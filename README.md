##Purpose
Will is built on python's alpine distribute; unfortunately using the smallest footprint
sometimes means we need base level packages added.  The will-base builds let us decouple
these base packages from the will dependencies. 
###Why? 
Segregating the base image gives us the chance to decouple changes and build containers
on rock-solid platforms. 


