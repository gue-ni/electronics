# Electronics Projects
## Wiener Linien Abfahrtsmonitor
![Title Image](https://github.com/gue-ni/electronics/blob/master/docs/img/img_2.jpg?raw=true)

#### Crontab
```
*/5 * * * * python /home/pi/arduino/pi/get_data.py # every 5 minutes
* * * * *  python /home/pi/arduino/pi/i2c_send.py  # every minute
```
#### Circuits
##### I2C
Pi GPiO 2 (SDA) - Arduino A4 (SDA)   
Pi GPiO 3 (SCL) - Arduino A5 (SCL)  
Pi GND 		- Arduino GND  

### Lora
#### Circuits
Arduino Pin 4 - E32 M0  
Arduino Pin 5 - E32 M1  
Arduino Pin 3 - 4k7 Ohm Resitor - E32 RXD  
Arduino Pin 2 - 4k7 Ohm Resitor - E32 TXD  
Arduino Pin 6 - 4k7 Ohm Resitor - E32 AUX  
Arduino 3.3V - E32 VCC   
Arduino GND - E32 GND  

