| **Method**                       | **Time to load part1** |
| -------------------------------- | ---------------------- |
| C. Simple inserts                | 36.73 seconds          |
| D. Drop Indexes and Constraints  | 35.11 seconds          |
| E. Disable Autocommit            | 8.394 seconds          |
| F. Use UNLOGGED table            | 7.982 seconds          |
| G. Temp Table with memory tuning | 8.251 seconds          |
| H. Batching                      |                        |
| I. copy_from                     |                        |

# Q&A

Try delaying the creation of these constraints/indexes until after the data set is loaded. Enter the resulting load time into the results table. Did this technique improve load performance?

Yea, IFF the index is not useful, we can drop the index to improve the performance.

How does load performance change if you do not set autocommit=True and instead explicitly commit all of the loaded data within a single transaction?

the speed become fast than before, cuz they also drop the commit, autocommit=True is faster

So update the [temp_buffers parameter](https://www.postgresql.org/docs/9.2/runtime-config-resource.html) to allow the database to use more memory for your temporary table. Rerun your load experiments. Did it make a difference?

Yes, cuz the memory is fast than this disk.