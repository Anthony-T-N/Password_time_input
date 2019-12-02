import time;

localTime = time.localtime(time.time());
localTime_str = str(localTime);
localTime_str = localTime_str.strip('time.struct_time()');
