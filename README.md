Kratos-VideoCompression

To display 3 live video feeds with no latency.
ROS-CV Bridge along with theora/compressed image transport is a very good option as used here.
The Repo includes 3 publisher files for the 3 cameras that publish data after compression, 3 subscriber files for each publisher, and two launch files to launch all cameras simultaeneously.
