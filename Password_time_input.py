import time;

localTime = time.localtime(time.time());
localTime_str = str(localTime);
localTime_str = localTime_str.strip("time.struct_time()");
# Now a list
localTime_str = localTime_str.split(" ");
print(localTime_str);

x = 0;
z = 0;
variable_1 = 0;
variable_2 = 0;
for i in localTime_str:
  i = i.split('=', 1)[-1];
  i = i[:-1];
  print(i);
  if (x == 2):
    variable_1 = i;
  if (x == 3):
    variable_2 = i;
  x = x + 1;
