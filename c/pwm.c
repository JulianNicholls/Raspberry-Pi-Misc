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

    while(1)
    {
        clrscr();

        printf("\n          Pulse Width Modulation demonstration\n\n");
        printf("    1 - Fade in and out\n");
        printf("    2 - Toggle PWM mode:    %s\n", (mode == 0) ? "Balanced" : "Mark / Space");
        printf("    3 - Set Duty Range:     %d\n", range);
        printf("    4 - Set Clock Divisor:  %d, Frequency: %.3f Hz\n",
               clock, ((BASE_CLOCK / clock) / range));
        printf("    5 - Set Duty Cycle:     %d\n", duty);
        printf("    6 - Exit\n\n");
        printf("        Enter selection: ");

        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                delta = 1;
                
                printf("\n\nDuty Value\n");

                for(int value = 0; value >= 0; value += delta)
                {
                    pwmWrite(PWM_PIN, value);
                    printf(" %5d\r", value);
                    delay(5);
                    if(value >= range)
                        delta = -1;
                }

                pwmWrite(PWM_PIN, 0);
                duty = 0;
                break;

            case 2:
                mode = !mode;

                pwmSetMode((mode == 0) ? PWM_MODE_BAL : PWM_MODE_MS);
                pwmWrite(PWM_PIN, duty);
                break;

            case 3:
                printf("\n\n        Enter the Duty Cycle steps (1-4096): ");
                scanf("%d", &range);
                pwmSetRange(range);

                if(duty > range)    // Adjust the value if the range is now less
                    duty = range;

                pwmWrite(PWM_PIN, duty);
                break;

            case 4:
                printf("\n\n        Enter the Clock (2-4095): ");
                scanf("%d", &clock);

                if(clock > 4095)    // Limit the clock divisor to 12 bits
                    clock = 4095;

                pwmSetClock(clock);
                pwmWrite(PWM_PIN, duty);
                break;

            case 5:
                printf("\n\n        Enter the Duty Cycle: ");
                scanf("%d", &duty);

                if(duty > range)    // Limit the entered value to the range
                    duty = range;

                pwmWrite(PWM_PIN, duty);
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
    pwmSetMode(PWM_MODE_MS);         // Much more useful than the default
    menu();

    return 0;
}

