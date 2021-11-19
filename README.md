# MapReduce-Execution-on-GCP

## 1. Copy of Your mapper.py code (or equivalent in another programming language) (25% of total grade)
```
public static class MaxTempMapper
        extends Mapper<LongWritable, Text, Text, IntWritable> {
            private static final int MISSING = 9999;

            public void map(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {
                    
                String line = value.toString();
                String date = line.substring(15, 23);
                int temp;
                if (line.charAt(87) == '+') {
                    temp = Integer.parseInt(line.substring(88, 92));
                }
                else {
                    temp = Integer.parseInt(line.substring(87, 92));
                }
                String quality = line.substring(92, 93);

                if(temp != MISSING && quality.matches("[01459]")) {
                    context.write(new Text(date), new IntWritable(temp));
                }
            }
        }
```

## 2. Copy of Your reducer.py code (or equivalent in another programming language) (25% of total grade)
```
public static class MaxTempReducer 
            extends Reducer<Text, IntWritable, Text, IntWritable> {

            public void reduce(Text key, Iterable<IntWritable> values, Context context)
                    throws IOException, InterruptedException {
                
                int maxValue = Integer.MIN_VALUE;
                for (IntWritable value : values) {
                    maxValue = Math.max(maxValue, value.get());
                }
                context.write(key, new IntWritable(maxValue));
            }
        }
```

## 3. Screenshot of the execution of Hadoop MapReduce Job in the terminal (25% of total grade)
#### steps
![alt text](https://github.com/xynicole/MapReduce-Execution-on-GCP/blob/main/Docker/1.jpeg)
![alt text](https://github.com/xynicole/MapReduce-Execution-on-GCP/blob/main/Docker/2.jpeg)
#### execution
![alt text](https://github.com/xynicole/MapReduce-Execution-on-GCP/blob/main/Docker/3.jpeg)
![alt text](https://github.com/xynicole/MapReduce-Execution-on-GCP/blob/main/Docker/4.jpeg)

## 4. Copy of your output file (after merging) containing the results (25% of total grade)
[result file ](https://github.com/xynicole/MapReduce-Execution-on-GCP/blob/main/Docker/result)

## Extra Credit: ▪ (+20%) Build GUI to upload the two data files from your local machine to GCP bucket automatically without having 

#### for my code, I removed my config json file and hide my bucket name 
https://user-images.githubusercontent.com/42621884/142592305-724745c2-6a6b-4c09-8774-9a7ccd7924f7.mp4


