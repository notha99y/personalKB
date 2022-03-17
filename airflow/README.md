# AirFlow
An Airflow pipeline is just a Python script that happens to define an Airflow DAG object

## DAG Definition file
Airflow Python script is really just a configuration file specifying the DAG's structure as code.

The actual tasks defined here will run in a different context from the context of the script. 

Different tasks run on different workers at different points in time, which means that this script cannot be used to cross communicate between tasks.

Note that for this purpose we have a more advanced feature called XComs.

People sometimes think of the DAG definition file as a place where they can do some actuall data processing - that is not the case at all! The script's purpose is to define a DAG object. It needs to evaluate quickly (seconds, not minutes) since the scheduler will execute it periodically to reflect the changes if any.

## Setting up task dependencies
We have tasks, `t1`, `t2`, `t3` that do not depend on each other. Here's a few ways you can define dependencies between them:
```python
t1.set_downstream(t2)
# this means that t2 will depend on t1 running successfully to run. It is equivalent to:
t2.set_upstream(t1)

# The bit shift operator can also be used to chain operations
t1 >> t2

# and the upstream dependency with the bit shift operator:
t2 << t1

# Chaining multiple dependencies become concise with the bit shift operator:
t1 >> t2 >> t3

# A list of tasks can also be set as dependencies. There operations all have the same effect:
t1.set_downstream([t2,t3])
t1 >> [t2, t3]
[t2, t3] << t1
```

# Useful links
- https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html
- https://www.youtube.com/watch?v=vvr_WNzEXBE


# Airflow Commands
- The `Standalone` command will initialise the database, make a user,  and start all components for you.
```bash
airflow standalone 
```

- run your first task instance
```bash
airflow tasks run example_bash_operator runme_0 2015-01-01
```

- run a backfill over 2 days
```bash
airflow dags backfill example_bash_operator \
    --start-date 2015-01-01 \
    --end-date 2015-01-02
```
- other commands
```bash
airflow db init

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

airflow webserver --port 8080

airflow scheduler
```

