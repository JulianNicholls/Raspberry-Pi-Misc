/****************************************************************************
 * PWM (Pulse-Width Modulation) demonstration.
 *
 * The wiringPi library must be installed.
 *
 * The PWM pin is physical pin 12 (GPIO18)
 *
 * The base clock for the PWM is 19.2MHz. This is divided down by the clock 
 * divisor and the range.
 *
 * compile with:
 *
 *     gcc -std=c99 -o pwm -l wiringPi pwm.c
 * or
 *     make
 *
 * run with:
 *
 *     sudo ./pwm
 */

#include <wiringPi.h>
#include <stdio.h>

#define clrscr() printf("\e[1;1H\e[2J")

const int       PWM_PIN     = 1;
const double    BASE_CLOCK  = 19.2e6;

const char*     modes[]     = {"Balanced", "Mark / Space"};

/****************************************************************************
 * Clock Frequency
 */

double frequency(int clock, int range)
{
    return (BASE_CLOCK / clock) / range;
}

/****************************************************************************
 * Clock Frequency
 */

char* freq_text(double freq)
{
    static char text[12];

    if(freq < 5000.0)
    {
        sprintf(text, "%.2f ", freq);
    }
    else if(freq < 1000000.0)
    {
        sprintf(text, "%.2f k", freq / 1000.0);
    }
    else
    {
        sprintf(text, "%.2f M", freq / 1000000.0);
    }

    return text;
}

/****************************************************************************
 * Menu
 */

void menu(void)
{
    int range   = 1024;
    int clock   = 32;
    int mode    = 1;
    int duty    = 0;
    int choice  = 0;
    int delta;

// Set up initial values

    pwmSetMode(PWM_MODE_MS);    // Mark / Space, rather than balanced default
    pwmSetRange(range);
    pwmSetClock(clock);
    pwmWrite(PWM_PIN, duty);

    while(1)
    {
        clrscr();

        printf("\n          Pulse Width Modulation demonstration\n\n");
        printf("    1 - Toggle PWM mode:    %s\n", modes[mode]);
        printf("    2 - Set Duty Range:     %d\n", range);
        printf("    3 - Set Clock Divisor:  %d, Frequency: %sHz\n", clock, freq_text(frequency(clock, range)));
        printf("    4 - Set Duty Cycle:     %d\n", duty);
        printf("    5 - Fade in and out\n");
        printf("    6 - Exit\n\n");
        printf("        Enter selection: ");

        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                mode = !mode;

                pwmSetMode((mode == 0) ? PWM_MODE_BAL : PWM_MODE_MS);
                pwmWrite(PWM_PIN, duty);
                break;

            case 2:
                printf("\n\n        Enter the Duty Cycle steps (1-4096): ");
                scanf("%d", &range);
                pwmSetRange(range);

                if(duty > range)    // Adjust the value if the range is now less
                    duty = range;

                pwmWrite(PWM_PIN, duty);
                break;

            case 3:
                printf("\n\n        Enter the Clock Divisor (2-4095): ");
                scanf("%d", &clock);

                // Constrain the entered value to the range 2 to 4095.

                if(clock < 2)
                    clock = 2;

                if(clock > 4095)
                    clock = 4095;

                pwmSetClock(clock);
                break;

            case 4:
                printf("\n\n        Enter the Duty Cycle: ");
                scanf("%d", &duty);

                // Constrain the value to the allowable range

                if(duty < 1)
                    duty = 0;

                if(duty > range)
                    duty = range;

                pwmWrite(PWM_PIN, duty);
                break;

            case 5:
                delta = 1;
                
                printf("\n\nDuty Value\n");

                for(int value = 0; value >= 0; value += delta)
                {
                    pwmWrite(PWM_PIN, value);
                    printf(" %5d\r", value);
                    delay(5);   // 5ms

                    if(value >= range)
                        delta = -1;
                }

                pwmWrite(PWM_PIN, 0);
                duty = 0;
                break;

            case 6:
                pwmWrite(PWM_PIN, 0);
                return;
        }
    }
}

int main(void)
{
    wiringPiSetup();
    pinMode(PWM_PIN, PWM_OUTPUT);

    menu();

    return 0;
}

