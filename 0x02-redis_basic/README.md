# Redis Basic

Redis is an Open-Sourc, in-memory data structure store used as a database, cache, and message broker. It is known for its speed and efficiency.

## Key Characteristics

1. In-memory Storage: Redis stores all its data in memory, which makes it extremely fast for read and write operations compared to traditional disk-based DB.
2. Data Structure: Unlike traditional DBs, Redis supports variety of data structures, such as strings, lists, sets, sorted sets, hashes, bitmaps, hyperloglogs, and geospatial indexes.
3. Persistence: Although primarily in-memory, it also supports persistence options to save data to disk, allowing you to recover data after a restart.
4. Replication and Scalability: Redis supports master-slave replication, and can be clustered to provide high availability and horizontal scalability
5. Single-Threaded: Redis operates on a singe thread, which simplifies concurrency issues and makes it easier to understand peformance characteristics
6. Atomic Operations: Redis supports atomic operations on its data structures, which makes it very powerful for complex operations in a single command
