# Electronics Projects
## Wiener Linien Departures
![Title Image](https://github.com/gue-ni/electronics/blob/master/docs/img/img_2.jpg?raw=true)

I used a raspberry pi and an arduino attached to an lcd to display when the tram leaves from the station near my apartment. The data comes from the official Wiener Linien API, which offers free 
real-time data on all of its services.


#### Crontab
```
*/5 * * * * python /home/pi/arduino/pi/wiener_linien_api.py # every 5 minutes
* * * * *  python /home/pi/arduino/pi/wiener_linien_i2c.py  # every minute
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

