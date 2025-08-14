import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # Exercise 1\.1
    $$
    p_1 = [1,2,1] \\
    p_2 = [4,2,2] \\
    p_3 = [6, 4, -1] \\
    p_4 = [5, 3, 0.5] \\
    q_1 = [1,2] \\
    q_2 = [2,1] \\
    p_3 = [-6, -4] \\
    p_4 = [10, 6]
    $$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Exercise 1\.2
    $$
    p_1 = [1,10,-3, 1] \\
    p_2 = [2,-4,1.1,2] \\
    p_3 = [0, 0, -1,10] \\
    p_4 = [-15, 3, 6, 3] \\
    q_1 = [1,10,-3] \\
    q_2 = [1,-2,0.55] \\
    q_3 = [0, 0, -0.1] \\
    q_4 = [-5, 1, 2] \\
    $$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Exercise 1\.3
    $$
    l =
    \left(
    \begin{array}{c}
    1 \\
    2 \\
    -3
    \end{array}
    \right)
    $$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Exercise 1\.4
    $$
    \mathbf{l} = \begin{bmatrix} 1 \\ 2 \\ -3 \end{bmatrix}
    $$

    we check for each homogeneous point $\mathbf{p}_i$ whether:

    $$
    \mathbf{l}^T \mathbf{p}_i = 0
    $$

    Let’s compute $\mathbf{l}^T \mathbf{p}_i$ for each point $\mathbf{p}_i$.

    ---

    ### Given Points:

    1. $\mathbf{p}_1 = \begin{bmatrix} 3 \\ 0 \\ 1 \end{bmatrix}$
    2. $\mathbf{p}_2 = \begin{bmatrix} 6 \\ 0 \\ 2 \end{bmatrix}$
    3. $\mathbf{p}_3 = \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix}$
    4. $\mathbf{p}_4 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$
    5. $\mathbf{p}_5 = \begin{bmatrix} 110 \\ -40 \\ 10 \end{bmatrix}$
    6. $\mathbf{p}_6 = \begin{bmatrix} 11 \\ 4 \\ 1 \end{bmatrix}$

    ---

    ### Compute $\mathbf{l}^T \mathbf{p}_i = [1, 2, -3] \cdot \mathbf{p}_i$

    #### 1. $\mathbf{p}_1$:

    $$
    1 \cdot 3 + 2 \cdot 0 + (-3) \cdot 1 = 3 + 0 - 3 = 0 \quad ✅ \text{on the line}
    $$

    #### 2. $\mathbf{p}_2$:

    $$
    1 \cdot 6 + 2 \cdot 0 + (-3) \cdot 2 = 6 + 0 - 6 = 0 \quad ✅ \text{on the line}
    $$

    #### 3. $\mathbf{p}_3$:

    $$
    1 \cdot 1 + 2 \cdot 1 + (-3) \cdot 2 = 1 + 2 - 6 = -3 \quad ❌ \text{not on the line}
    $$

    #### 4. $\mathbf{p}_4$:

    $$
    1 \cdot 1 + 2 \cdot 1 + (-3) \cdot 1 = 1 + 2 - 3 = 0 \quad ✅ \text{on the line}
    $$

    #### 5. $\mathbf{p}_5$:

    $$
    1 \cdot 110 + 2 \cdot (-40) + (-3) \cdot 10 = 110 - 80 - 30 = 0 \quad ✅ \text{on the line}
    $$

    #### 6. $\mathbf{p}_6$:

    $$
    1 \cdot 11 + 2 \cdot 4 + (-3) \cdot 1 = 11 + 8 - 3 = 16 \quad ❌ \text{not on the line}
    $$

    ---

    ### ✅ Final Answer: Points **on** the line

    $$
    \boxed{\mathbf{p}_1, \mathbf{p}_2, \mathbf{p}_4, \mathbf{p}_5}
    $$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Exercise 1\.5
    $$
    \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}
    \times
    \begin{bmatrix} -1 \\ 1 \\ -3 \end{bmatrix}
    = \begin{bmatrix} 2 \\ 4 \\ 2 \end{bmatrix}
    $$
    """
    )
    return


@app.cell
def _():
    import numpy as np
    a = np.array([1,1,-1])  
    b = np.array([-1,1,-3])
    #print the result    
    abcprod = np.cross(a,b)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Exercise 1\.6
    $$
    A = \begin{bmatrix}
    10 & 0 & 2 \\
    0 & 10 & -3 \\
    0 & 0 & 1
    \end{bmatrix} \\
    p = \begin{bmatrix} x \\ y \\ 1 \\ \end{bmatrix}
    $$


    $$
    q = A \times p = \begin{bmatrix} 10 x + 2 \\ 10 y - 3 \\ 1 \\ \end{bmatrix}
    $$

    - $A_{1,1}$ scales $x$
    - $A_{2,2}$ scales $y$
    - $A_{1,3}$ translates $x$
    - $A_{2,3}$ translates $y$

    """
    )
    return


@app.cell
def _(mo):
    mo.md(r""" """)
    return


if __name__ == "__main__":
    app.run()
