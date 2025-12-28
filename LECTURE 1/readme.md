## 1. Row Picture
- Each raw of the matrix acts as a single function.
- The dot product of a row and x creates one number in the result b.
- It is process of checking x against each row's rule to get a score.

## 2. Column Picture
- Each column of matrix is a direction.
- Scale each column by x and add them together (Linear Combination).
- Ax = b means "How do we mix these columns to reach the target b?"

## 3. Matrix Multiplication (AB = C)
- B is a collection of multiple input vectors.
- Run the column picture for each column of B to fill the columns of C.
- It is a batch process of Ax=b for many different x vectors at once.

## 4. Singularity
- Columns are stuck in the same plame (Linear Dependent).
- If the target b is outside that plane, we cannot reach it.
- The Space collapses, creating a dead zone where no solution x exists.