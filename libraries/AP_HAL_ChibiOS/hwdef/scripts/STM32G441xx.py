#!/usr/bin/env python
'''
tables for STM32G441xx MCUs
'''

# additional build information for ChibiOS
build = {
    "CHIBIOS_STARTUP_MK"  : "os/common/startup/ARMCMx/compilers/GCC/mk/startup_stm32g4xx.mk",
    "CHIBIOS_PLATFORM_MK" : "os/hal/ports/STM32/STM32G4xx/platform.mk"
    }

# MCU parameters
mcu = {
    # ram map, as list of (address, size-kb, flags)
    # flags of 1 means DMA-capable (DMA and BDMA)
    # flags of 2 means faster memory for CPU intensive work
    # flags of 4 means memory can be used for SDMMC DMA
    'RAM_MAP' : [
        (0x20000000, 22, 1), # SRAM1/SRAM2
        (0x10000000, 10, 2), # CCM
    ],

    'EXPECTED_CLOCK' : 160000000,

    'DEFINES' : {
        'STM32G4' : '1',
    }
}

# max pin package is 128
pincount = {
    'A': 16,
    'B': 16,
    'C': 16,
    'D': 16,
    'E': 16,
    'F': 16,
    'G': 16,
}
    
# no DMA map as we will dynamically allocate DMA channels using the DMAMUX
DMA_Map = None

AltFunction_map = {
	# format is PIN:FUNCTION : AFNUM
	# extracted from g441.txt
	"PA0:COMP1_OUT"     	:	8,
	"PA0:EVENTOUT"      	:	15,
	"PA0:TIM2_CH1"      	:	1,
	"PA0:TIM2_ETR"      	:	14,
	"PA0:TIM8_BKIN"     	:	9,
	"PA0:TIM8_ETR"      	:	10,
	"PA0:USART2_CTS"    	:	7,
	"PA0:USART2_NSS"    	:	7,
	"PA1:EVENTOUT"      	:	15,
	"PA1:RTC_REFIN"     	:	0,
	"PA1:TIM15_CH1N"    	:	9,
	"PA1:TIM2_CH2"      	:	1,
	"PA1:USART2_DE"     	:	7,
	"PA1:USART2_RTS"    	:	7,
	"PA2:COMP2_OUT"     	:	8,
	"PA2:EVENTOUT"      	:	15,
	"PA2:LPUART1_TX"    	:	12,
	"PA2:TIM15_CH1"     	:	9,
	"PA2:TIM2_CH3"      	:	1,
	"PA2:UCPD1_FRSTX1"  	:	14,
	"PA2:UCPD1_FRSTX2"  	:	14,
	"PA2:USART2_TX"     	:	7,
	"PA3:EVENTOUT"      	:	15,
	"PA3:LPUART1_RX"    	:	12,
	"PA3:SAI1_CK1"      	:	3,
	"PA3:SAI1_MCLK_A"   	:	13,
	"PA3:TIM15_CH2"     	:	9,
	"PA3:TIM2_CH4"      	:	1,
	"PA3:USART2_RX"     	:	7,
	"PA4:EVENTOUT"      	:	15,
	"PA4:I2S3_WS"       	:	6,
	"PA4:SAI1_FS_B"     	:	13,
	"PA4:SPI1_NSS"      	:	5,
	"PA4:SPI3_NSS"      	:	6,
	"PA4:TIM3_CH2"      	:	2,
	"PA4:USART2_CK"     	:	7,
	"PA5:EVENTOUT"      	:	15,
	"PA5:SPI1_SCK"      	:	5,
	"PA5:TIM2_CH1"      	:	1,
	"PA5:TIM2_ETR"      	:	2,
	"PA5:UCPD1_FRSTX1"  	:	14,
	"PA5:UCPD1_FRSTX2"  	:	14,
	"PA6:COMP1_OUT"     	:	8,
	"PA6:EVENTOUT"      	:	15,
	"PA6:LPUART1_CTS"   	:	12,
	"PA6:SPI1_MISO"     	:	5,
	"PA6:TIM16_CH1"     	:	1,
	"PA6:TIM1_BKIN"     	:	6,
	"PA6:TIM3_CH1"      	:	2,
	"PA6:TIM8_BKIN"     	:	4,
	"PA7:COMP2_OUT"     	:	8,
	"PA7:EVENTOUT"      	:	15,
	"PA7:SPI1_MOSI"     	:	5,
	"PA7:TIM17_CH1"     	:	1,
	"PA7:TIM1_CH1N"     	:	6,
	"PA7:TIM3_CH2"      	:	2,
	"PA7:TIM8_CH1N"     	:	4,
	"PA7:UCPD1_FRSTX1"  	:	14,
	"PA7:UCPD1_FRSTX2"  	:	14,
	"PA8:EVENTOUT"      	:	15,
	"PA8:I2C2_SDA"      	:	4,
	"PA8:I2C3_SCL"      	:	2,
	"PA8:I2S2_MCK"      	:	5,
	"PA8:RCC_MCO"       	:	0,
	"PA8:SAI1_CK2"      	:	12,
	"PA8:SAI1_SCK_A"    	:	14,
	"PA8:TIM1_CH1"      	:	6,
	"PA8:TIM4_ETR"      	:	10,
	"PA8:USART1_CK"     	:	7,
	"PA9:EVENTOUT"      	:	15,
	"PA9:I2C2_SCL"      	:	4,
	"PA9:I2C3_SMBA"     	:	2,
	"PA9:I2S3_MCK"      	:	5,
	"PA9:SAI1_FS_A"     	:	14,
	"PA9:TIM15_BKIN"    	:	9,
	"PA9:TIM1_CH2"      	:	6,
	"PA9:TIM2_CH3"      	:	10,
	"PA9:USART1_TX"     	:	7,
	"PA10:CRS_SYNC"     	:	3,
	"PA10:EVENTOUT"     	:	15,
	"PA10:I2C2_SMBA"    	:	4,
	"PA10:SAI1_D1"      	:	12,
	"PA10:SAI1_SD_A"    	:	14,
	"PA10:SPI2_MISO"    	:	5,
	"PA10:TIM17_BKIN"   	:	1,
	"PA10:TIM1_CH3"     	:	6,
	"PA10:TIM2_CH4"     	:	10,
	"PA10:TIM8_BKIN"    	:	11,
	"PA10:USART1_RX"    	:	7,
	"PA11:COMP1_OUT"    	:	8,
	"PA11:EVENTOUT"     	:	15,
	"PA11:CAN1_RX"    	:	9,
	"PA11:I2S2_SD"      	:	5,
	"PA11:SPI2_MOSI"    	:	5,
	"PA11:TIM1_BKIN2"   	:	12,
	"PA11:TIM1_CH1N"    	:	6,
	"PA11:TIM1_CH4"     	:	11,
	"PA11:TIM4_CH1"     	:	10,
	"PA11:USART1_CTS"   	:	7,
	"PA11:USART1_NSS"   	:	7,
	"PA12:COMP2_OUT"    	:	8,
	"PA12:EVENTOUT"     	:	15,
	"PA12:CAN1_TX"    	:	9,
	"PA12:I2S_CKIN"     	:	5,
	"PA12:TIM16_CH1"    	:	1,
	"PA12:TIM1_CH2N"    	:	6,
	"PA12:TIM1_ETR"     	:	11,
	"PA12:TIM4_CH2"     	:	10,
	"PA12:USART1_DE"    	:	7,
	"PA12:USART1_RTS"   	:	7,
	"PA13:EVENTOUT"     	:	15,
	"PA13:I2C1_SCL"     	:	4,
	"PA13:IR_OUT"       	:	5,
	"PA13:SAI1_SD_B"    	:	13,
    "PA13:JTMS-SWDIO"	:	0,
	"PA13:TIM16_CH1N"   	:	1,
	"PA13:TIM4_CH3"     	:	10,
	"PA13:USART3_CTS"   	:	7,
	"PA13:USART3_NSS"   	:	7,
	"PA14:EVENTOUT"     	:	15,
	"PA14:I2C1_SDA"     	:	4,
	"PA14:LPTIM1_OUT"   	:	1,
	"PA14:SAI1_FS_B"    	:	13,
    "PA14:JTCK-SWCLK"	:	0,
	"PA14:TIM1_BKIN"    	:	6,
	"PA14:TIM8_CH2"     	:	5,
	"PA14:USART2_TX"    	:	7,
	"PA15:EVENTOUT"     	:	15,
	"PA15:I2C1_SCL"     	:	4,
	"PA15:I2S3_WS"      	:	6,
	"PA15:SPI1_NSS"     	:	5,
	"PA15:SPI3_NSS"     	:	6,
	"PA15:SYS_JTDI"     	:	0,
	"PA15:TIM1_BKIN"    	:	9,
	"PA15:TIM2_CH1"     	:	1,
	"PA15:TIM2_ETR"     	:	14,
	"PA15:TIM8_CH1"     	:	2,
	"PA15:UART4_DE"     	:	8,
	"PA15:UART4_RTS"    	:	8,
	"PA15:USART2_RX"    	:	7,
	"PB0:EVENTOUT"      	:	15,
	"PB0:TIM1_CH2N"     	:	6,
	"PB0:TIM3_CH3"      	:	2,
	"PB0:TIM8_CH2N"     	:	4,
	"PB0:UCPD1_FRSTX1"  	:	14,
	"PB0:UCPD1_FRSTX2"  	:	14,
	"PB1:COMP4_OUT"     	:	8,
	"PB1:EVENTOUT"      	:	15,
	"PB1:LPUART1_DE"    	:	12,
	"PB1:LPUART1_RTS"   	:	12,
	"PB1:TIM1_CH3N"     	:	6,
	"PB1:TIM3_CH4"      	:	2,
	"PB1:TIM8_CH3N"     	:	4,
	"PB2:EVENTOUT"      	:	15,
	"PB2:I2C3_SMBA"     	:	4,
	"PB2:LPTIM1_OUT"    	:	1,
	"PB2:RTC_OUT2"      	:	0,
	"PB3:CRS_SYNC"      	:	3,
	"PB3:EVENTOUT"      	:	15,
	"PB3:I2S3_CK"       	:	6,
	"PB3:SAI1_SCK_B"    	:	14,
	"PB3:SPI1_SCK"      	:	5,
	"PB3:SPI3_SCK"      	:	6,
	"PB3:SYS_JTDO-SWO"  	:	0,
	"PB3:TIM2_CH2"      	:	1,
	"PB3:TIM3_ETR"      	:	10,
	"PB3:TIM4_ETR"      	:	2,
	"PB3:TIM8_CH1N"     	:	4,
	"PB3:USART2_TX"     	:	7,
	"PB4:EVENTOUT"      	:	15,
	"PB4:SAI1_MCLK_B"   	:	14,
	"PB4:SPI1_MISO"     	:	5,
	"PB4:SPI3_MISO"     	:	6,
	"PB4:SYS_JTRST"     	:	0,
	"PB4:TIM16_CH1"     	:	1,
	"PB4:TIM17_BKIN"    	:	10,
	"PB4:TIM3_CH1"      	:	2,
	"PB4:TIM8_CH2N"     	:	4,
	"PB4:USART2_RX"     	:	7,
	"PB5:EVENTOUT"      	:	15,
	"PB5:I2C1_SMBA"     	:	4,
	"PB5:I2C3_SDA"      	:	8,
	"PB5:I2S3_SD"       	:	6,
	"PB5:LPTIM1_IN1"    	:	11,
	"PB5:SAI1_SD_B"     	:	12,
	"PB5:SPI1_MOSI"     	:	5,
	"PB5:SPI3_MOSI"     	:	6,
	"PB5:TIM16_BKIN"    	:	1,
	"PB5:TIM17_CH1"     	:	10,
	"PB5:TIM3_CH2"      	:	2,
	"PB5:TIM8_CH3N"     	:	3,
	"PB5:USART2_CK"     	:	7,
	"PB6:COMP4_OUT"     	:	8,
	"PB6:EVENTOUT"      	:	15,
	"PB6:LPTIM1_ETR"    	:	11,
	"PB6:SAI1_FS_B"     	:	14,
	"PB6:TIM16_CH1N"    	:	1,
	"PB6:TIM4_CH1"      	:	2,
	"PB6:TIM8_BKIN2"    	:	10,
	"PB6:TIM8_CH1"      	:	5,
	"PB6:TIM8_ETR"      	:	6,
	"PB6:USART1_TX"     	:	7,
	"PB7:COMP3_OUT"     	:	8,
	"PB7:EVENTOUT"      	:	15,
	"PB7:I2C1_SDA"      	:	4,
	"PB7:LPTIM1_IN2"    	:	11,
	"PB7:TIM17_CH1N"    	:	1,
	"PB7:TIM3_CH4"      	:	10,
	"PB7:TIM4_CH2"      	:	2,
	"PB7:TIM8_BKIN"     	:	5,
	"PB7:UART4_CTS"     	:	14,
	"PB7:USART1_RX"     	:	7,
	"PB8:COMP1_OUT"     	:	8,
	"PB8:EVENTOUT"      	:	15,
	"PB8:CAN1_RX"     	:	9,
	"PB8:I2C1_SCL"      	:	4,
	"PB8:SAI1_CK1"      	:	3,
	"PB8:SAI1_MCLK_A"   	:	14,
	"PB8:TIM16_CH1"     	:	1,
	"PB8:TIM1_BKIN"     	:	12,
	"PB8:TIM4_CH3"      	:	2,
	"PB8:TIM8_CH2"      	:	10,
	"PB8:USART3_RX"     	:	7,
	"PB9:COMP2_OUT"     	:	8,
	"PB9:EVENTOUT"      	:	15,
	"PB9:CAN1_TX"     	:	9,
	"PB9:I2C1_SDA"      	:	4,
	"PB9:IR_OUT"        	:	6,
	"PB9:SAI1_D2"       	:	3,
	"PB9:SAI1_FS_A"     	:	14,
	"PB9:TIM17_CH1"     	:	1,
	"PB9:TIM1_CH3N"     	:	12,
	"PB9:TIM4_CH4"      	:	2,
	"PB9:TIM8_CH3"      	:	10,
	"PB9:USART3_TX"     	:	7,
	"PB10:EVENTOUT"     	:	15,
	"PB10:LPUART1_RX"   	:	8,
	"PB10:SAI1_SCK_A"   	:	14,
	"PB10:TIM1_BKIN"    	:	12,
	"PB10:TIM2_CH3"     	:	1,
	"PB10:USART3_TX"    	:	7,
	"PB11:EVENTOUT"     	:	15,
	"PB11:LPUART1_TX"   	:	8,
	"PB11:TIM2_CH4"     	:	1,
	"PB11:USART3_RX"    	:	7,
	"PB12:EVENTOUT"     	:	15,
	"PB12:I2C2_SMBA"    	:	4,
	"PB12:I2S2_WS"      	:	5,
	"PB12:LPUART1_DE"   	:	8,
	"PB12:LPUART1_RTS"  	:	8,
	"PB12:SPI2_NSS"     	:	5,
	"PB12:TIM1_BKIN"    	:	6,
	"PB12:USART3_CK"    	:	7,
	"PB13:EVENTOUT"     	:	15,
	"PB13:I2S2_CK"      	:	5,
	"PB13:LPUART1_CTS"  	:	8,
	"PB13:SPI2_SCK"     	:	5,
	"PB13:TIM1_CH1N"    	:	6,
	"PB13:USART3_CTS"   	:	7,
	"PB13:USART3_NSS"   	:	7,
	"PB14:COMP4_OUT"    	:	8,
	"PB14:EVENTOUT"     	:	15,
	"PB14:SPI2_MISO"    	:	5,
	"PB14:TIM15_CH1"    	:	1,
	"PB14:TIM1_CH2N"    	:	6,
	"PB14:USART3_DE"    	:	7,
	"PB14:USART3_RTS"   	:	7,
	"PB15:COMP3_OUT"    	:	3,
	"PB15:EVENTOUT"     	:	15,
	"PB15:I2S2_SD"      	:	5,
	"PB15:RTC_REFIN"    	:	0,
	"PB15:SPI2_MOSI"    	:	5,
	"PB15:TIM15_CH1N"   	:	2,
	"PB15:TIM15_CH2"    	:	1,
	"PB15:TIM1_CH3N"    	:	4,
	"PC0:EVENTOUT"      	:	15,
	"PC0:LPTIM1_IN1"    	:	1,
	"PC0:LPUART1_RX"    	:	8,
	"PC0:TIM1_CH1"      	:	2,
	"PC1:EVENTOUT"      	:	15,
	"PC1:LPTIM1_OUT"    	:	1,
	"PC1:LPUART1_TX"    	:	8,
	"PC1:SAI1_SD_A"     	:	13,
	"PC1:TIM1_CH2"      	:	2,
	"PC2:COMP3_OUT"     	:	3,
	"PC2:EVENTOUT"      	:	15,
	"PC2:LPTIM1_IN2"    	:	1,
	"PC2:TIM1_CH3"      	:	2,
	"PC3:EVENTOUT"      	:	15,
	"PC3:LPTIM1_ETR"    	:	1,
	"PC3:SAI1_D1"       	:	3,
	"PC3:SAI1_SD_A"     	:	13,
	"PC3:TIM1_BKIN2"    	:	6,
	"PC3:TIM1_CH4"      	:	2,
	"PC4:EVENTOUT"      	:	15,
	"PC4:I2C2_SCL"      	:	4,
	"PC4:TIM1_ETR"      	:	2,
	"PC4:USART1_TX"     	:	7,
	"PC5:EVENTOUT"      	:	15,
	"PC5:SAI1_D3"       	:	3,
	"PC5:TIM15_BKIN"    	:	2,
	"PC5:TIM1_CH4N"     	:	6,
	"PC5:USART1_RX"     	:	7,
	"PC6:EVENTOUT"      	:	15,
	"PC6:I2S2_MCK"      	:	6,
	"PC6:TIM3_CH1"      	:	2,
	"PC6:TIM8_CH1"      	:	4,
	"PC7:EVENTOUT"      	:	15,
	"PC7:I2S3_MCK"      	:	6,
	"PC7:TIM3_CH2"      	:	2,
	"PC7:TIM8_CH2"      	:	4,
	"PC8:EVENTOUT"      	:	15,
	"PC8:I2C3_SCL"      	:	8,
	"PC8:TIM3_CH3"      	:	2,
	"PC8:TIM8_CH3"      	:	4,
	"PC9:EVENTOUT"      	:	15,
	"PC9:I2C3_SDA"      	:	8,
	"PC9:I2S_CKIN"      	:	5,
	"PC9:TIM3_CH4"      	:	2,
	"PC9:TIM8_BKIN2"    	:	6,
	"PC9:TIM8_CH4"      	:	4,
	"PC10:EVENTOUT"     	:	15,
	"PC10:I2S3_CK"      	:	6,
	"PC10:SPI3_SCK"     	:	6,
	"PC10:TIM8_CH1N"    	:	4,
	"PC10:UART4_TX"     	:	5,
	"PC10:USART3_TX"    	:	7,
	"PC11:EVENTOUT"     	:	15,
	"PC11:I2C3_SDA"     	:	8,
	"PC11:SPI3_MISO"    	:	6,
	"PC11:TIM8_CH2N"    	:	4,
	"PC11:UART4_RX"     	:	5,
	"PC11:USART3_RX"    	:	7,
	"PC12:EVENTOUT"     	:	15,
	"PC12:I2S3_SD"      	:	6,
	"PC12:SPI3_MOSI"    	:	6,
	"PC12:TIM8_CH3N"    	:	4,
	"PC12:UCPD1_FRSTX1" 	:	14,
	"PC12:UCPD1_FRSTX2" 	:	14,
	"PC12:USART3_CK"    	:	7,
	"PC13:EVENTOUT"     	:	15,
	"PC13:TIM1_BKIN"    	:	2,
	"PC13:TIM1_CH1N"    	:	4,
	"PC13:TIM8_CH4N"    	:	6,
	"PC14:EVENTOUT"     	:	15,
	"PC15:EVENTOUT"     	:	15,
	"PD0:EVENTOUT"      	:	15,
	"PD0:CAN1_RX"     	:	9,
	"PD0:TIM8_CH4N"     	:	6,
	"PD1:EVENTOUT"      	:	15,
	"PD1:CAN1_TX"     	:	9,
	"PD1:TIM8_BKIN2"    	:	6,
	"PD1:TIM8_CH4"      	:	4,
	"PD2:EVENTOUT"      	:	15,
	"PD2:TIM3_ETR"      	:	2,
	"PD2:TIM8_BKIN"     	:	4,
	"PD3:EVENTOUT"      	:	15,
	"PD3:TIM2_CH1"      	:	2,
	"PD3:TIM2_ETR"      	:	2,
	"PD3:USART2_CTS"    	:	7,
	"PD3:USART2_NSS"    	:	7,
	"PD4:EVENTOUT"      	:	15,
	"PD4:TIM2_CH2"      	:	2,
	"PD4:USART2_DE"     	:	7,
	"PD4:USART2_RTS"    	:	7,
	"PD5:EVENTOUT"      	:	15,
	"PD5:USART2_TX"     	:	7,
	"PD6:EVENTOUT"      	:	15,
	"PD6:SAI1_D1"       	:	3,
	"PD6:SAI1_SD_A"     	:	13,
	"PD6:TIM2_CH4"      	:	2,
	"PD6:USART2_RX"     	:	7,
	"PD7:EVENTOUT"      	:	15,
	"PD7:TIM2_CH3"      	:	2,
	"PD7:USART2_CK"     	:	7,
	"PD8:EVENTOUT"      	:	15,
	"PD8:USART3_TX"     	:	7,
	"PD9:EVENTOUT"      	:	15,
	"PD9:USART3_RX"     	:	7,
	"PD10:EVENTOUT"     	:	15,
	"PD10:USART3_CK"    	:	7,
	"PD11:EVENTOUT"     	:	15,
	"PD11:USART3_CTS"   	:	7,
	"PD11:USART3_NSS"   	:	7,
	"PD12:EVENTOUT"     	:	15,
	"PD12:TIM4_CH1"     	:	2,
	"PD12:USART3_DE"    	:	7,
	"PD12:USART3_RTS"   	:	7,
	"PD13:EVENTOUT"     	:	15,
	"PD13:TIM4_CH2"     	:	2,
	"PD14:EVENTOUT"     	:	15,
	"PD14:TIM4_CH3"     	:	2,
	"PD15:EVENTOUT"     	:	15,
	"PD15:SPI2_NSS"     	:	6,
	"PD15:TIM4_CH4"     	:	2,
	"PE0:EVENTOUT"      	:	15,
	"PE0:TIM16_CH1"     	:	4,
	"PE0:TIM4_ETR"      	:	2,
	"PE0:USART1_TX"     	:	7,
	"PE1:EVENTOUT"      	:	15,
	"PE1:TIM17_CH1"     	:	4,
	"PE1:USART1_RX"     	:	7,
	"PE2:EVENTOUT"      	:	15,
	"PE2:SAI1_CK1"      	:	3,
	"PE2:SAI1_MCLK_A"   	:	13,
	"PE2:SYS_TRACECLK"  	:	0,
	"PE2:TIM3_CH1"      	:	2,
	"PE3:EVENTOUT"      	:	15,
	"PE3:SAI1_SD_B"     	:	13,
	"PE3:SYS_TRACED0"   	:	0,
	"PE3:TIM3_CH2"      	:	2,
	"PE4:EVENTOUT"      	:	15,
	"PE4:SAI1_D2"       	:	3,
	"PE4:SAI1_FS_A"     	:	13,
	"PE4:SYS_TRACED1"   	:	0,
	"PE4:TIM3_CH3"      	:	2,
	"PE5:EVENTOUT"      	:	15,
	"PE5:SAI1_CK2"      	:	3,
	"PE5:SAI1_SCK_A"    	:	13,
	"PE5:SYS_TRACED2"   	:	0,
	"PE5:TIM3_CH4"      	:	2,
	"PE6:EVENTOUT"      	:	15,
	"PE6:SAI1_D1"       	:	3,
	"PE6:SAI1_SD_A"     	:	13,
	"PE6:SYS_TRACED3"   	:	0,
	"PE7:EVENTOUT"      	:	15,
	"PE7:SAI1_SD_B"     	:	13,
	"PE7:TIM1_ETR"      	:	2,
	"PE8:EVENTOUT"      	:	15,
	"PE8:SAI1_SCK_B"    	:	13,
	"PE8:TIM1_CH1N"     	:	2,
	"PE9:EVENTOUT"      	:	15,
	"PE9:SAI1_FS_B"     	:	13,
	"PE9:TIM1_CH1"      	:	2,
	"PE10:EVENTOUT"     	:	15,
	"PE10:SAI1_MCLK_B"  	:	13,
	"PE10:TIM1_CH2N"    	:	2,
	"PE11:EVENTOUT"     	:	15,
	"PE11:TIM1_CH2"     	:	2,
	"PE12:EVENTOUT"     	:	15,
	"PE12:TIM1_CH3N"    	:	2,
	"PE13:EVENTOUT"     	:	15,
	"PE13:TIM1_CH3"     	:	2,
	"PE14:EVENTOUT"     	:	15,
	"PE14:TIM1_BKIN2"   	:	6,
	"PE14:TIM1_CH4"     	:	2,
	"PE15:EVENTOUT"     	:	15,
	"PE15:TIM1_BKIN"    	:	2,
	"PE15:TIM1_CH4N"    	:	6,
	"PE15:USART3_RX"    	:	7,
	"PF0:EVENTOUT"      	:	15,
	"PF0:I2C2_SDA"      	:	4,
	"PF0:I2S2_WS"       	:	5,
	"PF0:SPI2_NSS"      	:	5,
	"PF0:TIM1_CH3N"     	:	6,
	"PF1:EVENTOUT"      	:	15,
	"PF1:I2S2_CK"       	:	5,
	"PF1:SPI2_SCK"      	:	5,
	"PF2:EVENTOUT"      	:	15,
	"PF2:I2C2_SMBA"     	:	4,
	"PF9:EVENTOUT"      	:	15,
	"PF9:SAI1_FS_B"     	:	13,
	"PF9:SPI2_SCK"      	:	5,
	"PF9:TIM15_CH1"     	:	3,
	"PF10:EVENTOUT"     	:	15,
	"PF10:SAI1_D3"      	:	13,
	"PF10:SPI2_SCK"     	:	5,
	"PF10:TIM15_CH2"    	:	3,
	"PG10:EVENTOUT"     	:	15,
	"PG10:RCC_MCO"      	:	0,
}

ADC1_map = {
    # format is PIN : ADC1_CHAN
    "PA0"   :    1,
    "PA1"   :    2,
    "PA2"   :    3,
    "PA3"   :    4,
    "PB14"  :   5,
    "PC0"   :   6,
    "PC1"   :   7,
    "PC2"   :   8,
    "PC3"   :   9,
    "PF0"   :  10,
    "PB12"  :  11,
    "PB1"   :  12,
    "PB11"  :  14,
    "PB0"   :  15,
}
