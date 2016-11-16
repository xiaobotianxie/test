<configuration> /*hadoop map-reduce         3     mapred-site.xml   "mapreduce.framework.name"         "classic" "yarn"  "local"*/
<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>
/*MapReduce JobHistory Server  */
<property>
<name>mapreduce.jobhistory.address</name>
<value>Master 10020</value>
</property>
/*MapReduce JobHistory Server Web UI  */
<property>
<name>mapreduce.jobhistory.webapp.address</name>
<value>Master 19888</value>
</property>
</configuration>
