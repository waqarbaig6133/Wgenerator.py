## W Generator
The aim of this project is to understand the patterns behind generating the letter W in ascii form with any value S, where S is the height of the letter. There are many ways to make this, but this is my mediocre approach to it.
##
First, we need to identify the similarities and differences between the W at different heights.
For instance, two Ws that are 5 and 6 spaces high.
```
s = 5

 *             *
  *     *     *
   *   * *   *
    * *   * *
     *     *

s = 6

 *                 *
  *       *       *
   *     * *     * 
    *   *   *   *
     * *     * *
      *       *

```
First thing to note is that when generating a symmetrical W, each colomn or space has to have 1 character (for better results, use stars). 
