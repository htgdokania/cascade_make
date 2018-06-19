# cascade_make
make custom cascades 
steps to follow:
1. first get your neg files ready
2. open 'neg create.py' and run to generate bg.txt file
3. create empty folders named 'info' and 'data' at the same place as bg.txt is created
4. next, paste the sample positive image say 'test.png' in the same folder as the bg.txt is present
5. next,we creat many sample positives using opencv command .for that open terminal and type:

 opencv_createsamples -img test.png -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 3000

6. next we create a vector file using the command:

opencv_createsamples -info info/info.lst -num 3000 -w 20 -h 20 -vec positives.vec 

7. next train the cascade using command:

opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 2800 -numNeg 900 -numStages 10 -w 20 -h 20

8. once training is complete open the data folder  and cascade.xml will be present 


use the cascade file in your projects

