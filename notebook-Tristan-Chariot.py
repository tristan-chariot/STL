import marimo

__generated_with = "0.9.17"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("""#3D Geometry File Formats""")
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## About STL

        STL is a simple file format which describes 3D objects as a collection of triangles.
        The acronym STL stands for "Simple Triangle Language", "Standard Tesselation Language" or "STereoLitography"[^1].

        [^1]: STL was invented for – and is still widely used – for 3D printing.
        """
    )
    return


@app.cell
def __(mo, show):
    mo.show_code(show("data/teapot.stl", theta=45.0, phi=30.0, scale=2))
    return


@app.cell
def __(mo):
    with open("data/teapot.stl", mode="rt", encoding="utf-8") as _file:
        teapot_stl = _file.read()

    teapot_stl_excerpt = teapot_stl[:723] + "..." + teapot_stl[-366:]

    mo.md(
        f"""
    ## STL ASCII Format

    The `data/teapot.stl` file provides an example of the STL ASCII format. It is quite large (more than 60000 lines) and looks like that:
    """
    +
    f"""```
    {teapot_stl_excerpt}
    ```
    """
    +

    """
    """
    )
    return teapot_stl, teapot_stl_excerpt


@app.cell
def __(mo):
    mo.md(f"""

      - Study the [{mo.icon("mdi:wikipedia")} STL (file format)](https://en.wikipedia.org/wiki/STL_(file_format)) page (or other online references) to become familiar the format.

      - Create a STL ASCII file `"data/cube.stl"` that represents a cube of unit length  
        (💡 in the simplest version, you will need 12 different facets).

      - Display the result with the function `show` (make sure to check different angles).
    """)
    return


@app.cell
def __():
    cube_stl = '''
    solide cube
        facet normal 0.0 0.0 -1.0
            outer loop 
                vertex 0.0 0.0 0.0
                vertex 1.0 1.0 0.0
                vertex 1.0 0.0 0.0
            endloop
        endfacet
        facet normal 0.0 0.0 -1.0 
            outer loop 
                vertex 1.0 0.0 0.0
                vertex 0.0 1.0 0.0
                vertex 1.0 1.0 0.0
            endloop
        endfacet
        facet normal 0.0 0.0 1.0
            outer loop 
                vertex 0.0 0.0 1.0
                vertex 1.0 0.0 1.0
                vertex 1.0 1.0 1.0
            endloop
        endfacet
        facet normal 0.0 0.0 1.0 
            outer loop 
                vertex 1.0 0.0 1.0
                vertex 1.0 1.0 1.0
                vertex 0.0 1.0 1.0
            endloop
        endfacet
        facet normal -1.0 0.0 0.0 
            outer loop 
                vertex 0.0 0.0 0.0
                vertex 0.0 0.0 1.0
                vertex 0.0 1.0 0.0
            endloop
        endfacet
        facet normal -1.0 0.0 0.0 
            outer loop 
                vertex 0.0 1.0 1.0
                vertex 0.0 1.0 0.0
                vertex 0.0 0.0 1.0
            endloop
        endfacet
        facet normal 1.0 0.0 0.0 
            outer loop 
                vertex 1.0 0.0 0.0
                vertex 1.0 1.0 0.0
                vertex 1.0 0.0 1.0
            endloop
        endfacet
        facet normal 1.0 0.0 0.0 
            outer loop 
                vertex 1.0 1.0 1.0
                vertex 1.0 0.0 1.0
                vertex 1.0 1.0 0.0
            endloop
        endfacet
        facet normal 0.0 -1.0 0.0 
            outer loop 
                vertex 0.0 0.0 0.0
                vertex 1.0 0.0 0.0
                vertex 0.0 0.0 1.0
            endloop
        endfacet   
        facet normal 0.0 -1.0 0.0 
            outer loop 
                vertex 1.0 0.0 1.0
                vertex 0.0 0.0 1.0
                vertex 1.0 0.0 0.0
            endloop
        endfacet
            facet normal 0.0 1.0 0.0 
            outer loop 
                vertex 0.0 1.0 0.0
                vertex 0.0 1.0 1.0
                vertex 1.0 1.0 0.0
            endloop
        endfacet   
        facet normal 0.0 1.0 0.0 
            outer loop 
                vertex 1.0 1.0 1.0
                vertex 1.0 1.0 0.0
                vertex 0.0 1.0 1.0
            endloop
        endfacet 
    endsolid cube
    '''

    # solid  début de l'objet 3D
    # endsolid fin de l'ojet 3D
    # facet normal désigne les coordonnées du vecteur normal à la surface triangulaire
    # outer loop : début définition des 3 sommets du triangle
    # vertex definit un sommet su triangle avec ses 3 coordonnées
    # end facet : fin de la définition de la face
    # end loop : fin définition des 3 somets du triangle
    return (cube_stl,)


@app.cell
def __(cube_stl):
    with open("data/cube.stl", "wt", encoding="utf-8") as fichier_cube :
        fichier_cube.write(cube_stl)
    return (fichier_cube,)


@app.cell
def __(mo, show):
    mo.show_code(show("data/cube.stl", theta=+30.0, phi=40, scale=1))
    return


@app.cell
def __(mo):
    mo.md(r"""## STL & NumPy""")
    return


@app.cell
def __(mo):
    mo.md(rf"""

    ### NumPy to STL

    Implement the following function:

    ```python
    def make_STL(triangles, normals=None, name=""):
        pass # 🚧 TODO!
    ```

    #### Parameters

      - `triangles` is a NumPy array of shape `(n, 3, 3)` and data type `np.float32`,
         which represents a sequence of `n` triangles (`triangles[i, j, k]` represents 
         is the `k`th coordinate of the `j`th point of the `i`th triangle)

      - `normals` is a NumPy array of shape `(n, 3)` and data type `np.float32`;
         `normals[i]` represents the outer unit normal to the `i`th facet.
         If `normals` is not specified, it should be computed from `triangles` using the 
         [{mo.icon("mdi:wikipedia")} right-hand rule](https://en.wikipedia.org/wiki/Right-hand_rule).

      - `name` is the (optional) solid name embedded in the STL ASCII file.

    #### Returns

      - The STL ASCII description of the solid as a string.

    #### Example

    Given the two triangles that make up a flat square:

    ```python

    square_triangles = np.array(
        [
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
            [[1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]],
        ],
        dtype=np.float32,
    )
    ```

    then printing `make_STL(square_triangles, name="square")` yields
    ```
    solid square
      facet normal 0.0 0.0 1.0
        outer loop
          vertex 0.0 0.0 0.0
          vertex 1.0 0.0 0.0
          vertex 0.0 1.0 0.0
        endloop
      endfacet
      facet normal 0.0 0.0 1.0
        outer loop
          vertex 1.0 1.0 0.0
          vertex 0.0 1.0 0.0
          vertex 1.0 0.0 0.0
        endloop
      endfacet
    endsolid square
    ```

    """)
    return


@app.cell
def __(np):
    def make_STL(triangles, normals=None, name=""):
        STL_ASCII_description = ""
        STL_ASCII_description += "solid"
        STL_ASCII_description += " "+name
        for t in range(len(triangles)):
            STL_ASCII_description += "\n \t facet normal"
            if normals[t] is not None:
                for k in range(3):
                    STL_ASCII_description += f" {normals[t][k]}"
            else: # on utilise la règle de la main doite
                p0 = np.array([triangles[t][0][k] for k in range(3)])
                p1 = np.array([triangles[t][1][k] for k in range(3)])
                p2 = np.array([triangles[t][2][k] for k in range(3)])
                v1 = p1 - p0
                v2 = p2 - p0
                v_normal = np.cross(v1, v2)
                v_normal = v_normal/np.linalg.norm(v_normal)
                for k in range(3):
                    STL_ASCII_description += f" {v_normal[k]}"
            STL_ASCII_description += "\n \t \t outer loop" 
            for p in range(3):
                STL_ASCII_description += "\n \t \t \t vertex"
                for k in range(3):
                    STL_ASCII_description += f" {triangles[t][p][k]}"
            STL_ASCII_description += "\n \t \t endloop"
            STL_ASCII_description += "\n \t endfacet"
        STL_ASCII_description += "\n endsolid"
        STL_ASCII_description += " "+name
        return STL_ASCII_description
    return (make_STL,)


@app.cell
def __(make_STL, np):
    square_triangles = np.array(
        [
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
            [[1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]],
        ],
        dtype=np.float32,
    )

    square_normals = [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]

    make_STL(square_triangles, square_normals, name="square")
    return square_normals, square_triangles


@app.cell
def __(make_STL, mo, show, square_normals, square_triangles):
    text_square_stl = make_STL(square_triangles, square_normals, name="square")
    with open("data/square_make_STL.stl", mode="wt", encoding="utf-8") as file_c:
        file_c.write(text_square_stl)
    mo.show_code(show("data/square_make_STL.stl", theta=45.0, phi=30.0, scale=1.5))
    return file_c, text_square_stl


@app.cell
def __(mo):
    mo.md(
        """
        ### STL to NumPy

        Implement a `tokenize` function


        ```python
        def tokenize(stl):
            pass # 🚧 TODO!
        ```

        that is consistent with the following documentation:


        #### Parameters

          - `stl`: a Python string that represents a STL ASCII model.

        #### Returns

          - `tokens`: a list of STL keywords (`solid`, `facet`, etc.) and `np.float32` numbers.

        #### Example

        For the ASCII representation the square `data/square.stl`, printing the tokens with

        ```python
        with open("data/square.stl", mode="rt", encoding="us-ascii") as square_file:
            square_stl = square_file.read()
        tokens = tokenize(square_stl)
        print(tokens)
        ```

        yields

        ```python
        ['solid', 'square', 'facet', 'normal', np.float32(0.0), np.float32(0.0), np.float32(1.0), 'outer', 'loop', 'vertex', np.float32(0.0), np.float32(0.0), np.float32(0.0), 'vertex', np.float32(1.0), np.float32(0.0), np.float32(0.0), 'vertex', np.float32(0.0), np.float32(1.0), np.float32(0.0), 'endloop', 'endfacet', 'facet', 'normal', np.float32(0.0), np.float32(0.0), np.float32(1.0), 'outer', 'loop', 'vertex', np.float32(1.0), np.float32(1.0), np.float32(0.0), 'vertex', np.float32(0.0), np.float32(1.0), np.float32(0.0), 'vertex', np.float32(1.0), np.float32(0.0), np.float32(0.0), 'endloop', 'endfacet', 'endsolid', 'square']
        ```
        """
    )
    return


@app.cell
def __(np):
    def tokenize(stl):
        tokens = []
        Ls_stl = stl.split()
        for char in Ls_stl:
            try: # Cas où la chaîne de caractère est un flottant
                nombre = np.float32(char)
                tokens.append(nombre)
            except : # Cas où la chaîne de caractère n'est pas un flottant
                tokens.append(char)
        return tokens
    return (tokenize,)


@app.cell
def __(tokenize):
    with open("data/square.stl", mode="rt", encoding="us-ascii") as square_file_c:
        square_stl = square_file_c.read()
    tokens = tokenize(square_stl)
    print(tokens)
    return square_file_c, square_stl, tokens


@app.cell
def __(mo):
    mo.md(
        """
        Implement a `parse` function


        ```python
        def parse(tokens):
            pass # 🚧 TODO!
        ```

        that is consistent with the following documentation:


        #### Parameters

          - `tokens`: a list of tokens

        #### Returns

        A `triangles, normals, name` triple where

          - `triangles`: a `(n, 3, 3)` NumPy array with data type `np.float32`,

          - `normals`: a `(n, 3)` NumPy array with data type `np.float32`,

          - `name`: a Python string.

        #### Example

        For the ASCII representation `square_stl` of the square,
        tokenizing then parsing

        ```python
        with open("data/square.stl", mode="rt", encoding="us-ascii") as square_file:
            square_stl = square_file.read()
        tokens = tokenize(square_stl)
        triangles, normals, name = parse(tokens)
        print(repr(triangles))
        print(repr(normals))
        print(repr(name))
        ```

        yields

        ```python
        array([[[0., 0., 0.],
                [1., 0., 0.],
                [0., 1., 0.]],

               [[1., 1., 0.],
                [0., 1., 0.],
                [1., 0., 0.]]], dtype=float32)
        array([[0., 0., 1.],
               [0., 0., 1.]], dtype=float32)
        'square'
        ```
        """
    )
    return


@app.cell
def __(np):
    def parse(tokens):
        triangles = []
        normals = []
        name = ""
        for i in range(len(tokens)):
            if tokens[i] == 'solid' and tokens[i+1] != 'facet':
                name += tokens[i+1]
            elif tokens[i] == 'normal':
                normals.append([tokens[i+1], tokens[i+2], tokens[i+3]])
            elif tokens[i] == 'loop':
                triangles.append([[tokens[i+k] for k in range(2,5)],[tokens[i+k] for k in range(6,9)],[tokens[i+k] for k in range(10,13)]])
        triangles = np.array(triangles, dtype=np.float32)
        normals = np.array(normals, dtype=np.float32)
        return triangles, normals, name
    return (parse,)


@app.cell
def __(parse, tokenize):
    with open("data/square.stl", mode="rt", encoding="us-ascii") as square_file2:
        square_stl2 = square_file2.read()
    tokens2 = tokenize(square_stl2)
    triangles, normals, name = parse(tokens2)
    print(repr(triangles))
    print(repr(normals))
    print(repr(name))
    return name, normals, square_file2, square_stl2, tokens2, triangles


@app.cell
def __(mo):
    mo.md(
        rf"""
    ## Rules & Diagnostics



        Make diagnostic functions that check whether a STL model satisfies the following rules

          - **Positive octant rule.** All vertex coordinates are non-negative.

          - **Orientation rule.** All normals are (approximately) unit vectors and follow the [{mo.icon("mdi:wikipedia")} right-hand rule](https://en.wikipedia.org/wiki/Right-hand_rule).

          - **Shared edge rule.** Each triangle edge appears exactly twice.

          - **Ascending rule.** the z-coordinates of (the barycenter of) each triangle are a non-decreasing sequence.

    When the rule is broken, make sure to display some sensible quantitative measure of the violation (in %).

    For the record, the `data/teapot.STL` file:

      - 🔴 does not obey the positive octant rule,
      - 🟠 almost obeys the orientation rule, 
      - 🟢 obeys the shared edge rule,
      - 🔴 does not obey the ascending rule.

    Check that your `data/cube.stl` file does follow all these rules, or modify it accordingly!

    """
    )
    return


@app.cell
def __(np, parse, tokenize, triangle):
    def diagnostic(fichier_stl):
        ''' prend en arguement un fichier STL
        Affiche pour chaque règle si elle est vérifée ou non
        '''
        with open(fichier_stl, mode="rt", encoding="utf-8") as file_stl:
            stl = file_stl.read()
        triangles, normals, name = parse(tokenize(stl))
        coord_vertex = triangles[:, :, -1].reshape(1,1,3*len(triangles))

        # Positive octant rule
        coord_vertex_neg = (coord_vertex < 0)
        nb_coord_vertex_neg = np.sum(coord_vertex_neg)
        if nb_coord_vertex_neg == 0:
            print('🟢 Obeys the positive octant rule')
        else:
            print(f'🔴 Does not obey the positive octant rule, avec une violation de {100 * nb_coord_vertex_neg/len(triangle)}%')

        # Orientation rule
        normes = np.linalg.norm(normals, axis=1)
        normes_false = (normes-1 != 0)
        nb_normes_false = np.sum(normes_false)
        Ls_v_normal = []
        for t in range(len(triangles)):
            p0 = np.array([triangles[t][0][k] for k in range(3)])
            p1 = np.array([triangles[t][1][k] for k in range(3)])
            p2 = np.array([triangles[t][2][k] for k in range(3)])
            v1 = p1 - p0
            v2 = p2 - p0
            v_normal = np.cross(v1, v2)
            v_normal = v_normal/np.linalg.norm(v_normal)
            Ls_v_normal.append(v_normal)
        Ls_v_normal = np.array(Ls_v_normal, dtype=np.float32)
        v_normaux_false = (Ls_v_normal != normals)
        nb_v_normaux_false = np.sum(v_normaux_false)
        if nb_v_normaux_false == 0 and nb_normes_false == 0:
            print('🟢 Obeys the orientation rule')
        elif nb_v_normaux_false == 0 and nb_normes_false != 0:
            print(f'🟠 Almost obeys the orientation rule, avec {100 * nb_normes_false/len(normes)}% de vecteurs non unitaires')
        elif nb_v_normaux_false != 0 and nb_normes_false == 0:
            print(f'🟠 Almost obeys the orientation rule, avec {100 *  nb_v_normaux_false/len(normals)}% de vecteurs normaux faux')
        else:
            print(f'🔴 Does not obeys the orientation rule avec {100 *  nb_v_normaux_false/len(normals)}% de vecteurs normaux faux et  avec {100 * nb_normes_false/len(normes)}% de vecteurs non unitaires' )

        # Shared edge rule
        vertex = coord_vertex.reshape(len(triangles), 3)
        vertex = np.array(vertex, dtype=np.float32)
        Ls_vertex_u = np.unique(vertex, axis=0)
        Ls_vertex_u, Ls_nb_arrete = np.unique(vertex, axis=0, return_counts=True)
        nb_arrete_false = np.sum(Ls_nb_arrete != 2)
        if nb_arrete_false == 0:
            print('🟢 Obeys the orientation rule')
        else :
             print(f"🔴 Does not obeys the shared edge rule avec {100 *  nb_arrete_false/len(vertex)}% d'arrêtes qui ne sont pas présente éxactement deux fois")

        # Ascending rule
        z_coordinate = coord_vertex[2::3]
        Ls_diff_successive = np.diff(z_coordinate)
        nb_diff_successive_false = np.sum(Ls_diff_successive < 0)
        if nb_diff_successive_false == 0:
            print('🟢 Obeys the ascending rule')
        else :
             print(f"🔴 Does not obeys the orientation rule avec {100 *  nb_diff_successive_false/len(Ls_diff_successive)}% de'arrêtes qui ne sont pas présente éxactement deux fois")
    return (diagnostic,)


@app.cell
def __(diagnostic):
    diagnostic("data/cube.stl")
    return


@app.cell
def __(mo):
    mo.md(
    rf"""
    ## OBJ Format

    The OBJ format is an alternative to the STL format that looks like this:

    ```
    # OBJ file format with ext .obj
    # vertex count = 2503
    # face count = 4968
    v -3.4101800e-003 1.3031957e-001 2.1754370e-002
    v -8.1719160e-002 1.5250145e-001 2.9656090e-002
    v -3.0543480e-002 1.2477885e-001 1.0983400e-003
    v -2.4901590e-002 1.1211138e-001 3.7560240e-002
    v -1.8405680e-002 1.7843055e-001 -2.4219580e-002
    ...
    f 2187 2188 2194
    f 2308 2315 2300
    f 2407 2375 2362
    f 2443 2420 2503
    f 2420 2411 2503
    ```

    This content is an excerpt from the `data/bunny.obj` file.

    """
    )
    return


@app.cell
def __(mo, show):
    mo.show_code(show("data/bunny.obj", scale="1.5"))
    return


@app.cell
def __(mo):
    mo.md(
        """
        Study the specification of the OBJ format (search for suitable sources online),
        then develop a `OBJ_to_STL` function that is rich enough to convert the OBJ bunny file into a STL bunny file.
        """
    )
    return


@app.cell
def __(make_STL, np):
    def obj_to_stl(obj_filename, stl_filename, name):
        vertex = []
        normals = []
        with open(obj_filename, mode="rt", encoding="utf-8") as file_stl:
            obj_text = file_stl.read()
        obj_text_split = obj_text.split() 
        for k in range(len(obj_text_split)):
            if obj_text_split[k] == 'v':
                vertex.append([np.float32(obj_text_split[k + i]) for i in range(1,4)])
            elif obj_text_split[k] == 'f':
                normals.append([np.float32(obj_text_split[k + i]) for i in range(1,4)])
        vertex = np.array(vertex, dtype=np.float32)
        normals = np.array(normals, dtype=np.float32) 
        triangles = []
        cpt_triangle = 0
        for liste_vertex in vertex:
            triangles.append([[cpt_triangle, k, liste_vertex[k]] for k in range(3)])
            cpt_triangle += 1
        triangles = np.array(triangles, dtype=np.float32)
        normals = np.array(normals, dtype=np.float32)
        stl_text = make_STL(triangles, normals, name)
        with open(stl_filename, 'wt', encoding="utf-8") as file2:
            file2.write(stl_text)
    return (obj_to_stl,)


@app.cell
def __(obj_to_stl):
    obj_to_stl('data/bunny.obj', 'data/bunny.stl', 'bunny')
    return


@app.cell
def __(mo, show):
    mo.show_code(show("data/bunny.stl", scale="1.5"))
    # étrange bunny ne s'affiche pas
    return


@app.cell
def __(mo, obj_to_stl, show):
    text_obj = """v -3.4101800e-003 1.3031957e-001 2.1754370e-002
    v -8.1719160e-002 1.5250145e-001 2.9656090e-002
    v -3.0543480e-002 1.2477885e-001 1.0983400e-003
    v -2.4901590e-002 1.1211138e-001 3.7560240e-002
    v -1.8405680e-002 1.7843055e-001 -2.4219580e-002
    v 1.9067940e-002 1.2144925e-001 3.1968440e-002
    v 6.0412000e-003 1.2494359e-001 3.2652890e-002
    v -1.3469030e-002 1.6299355e-001 -1.2000020e-002
    v -3.4393240e-002 1.7236688e-001 -9.8213000e-004
    v -8.4314160e-002 1.0957263e-001 3.7097300e-003
    f 1069 1647 1578
    f 1058 909 939
    f 421 1176 238
    f 1055 1101 1042
    f 238 1059 1126
    f 1254 30 1261
    f 1065 1071 1
    f 1037 1130 1120
    f 1570 2381 1585
    f 2434 2502 2473
    """
    with open("data/bunny_short.obj", mode="wt", encoding="utf-8") as file_obj:
        file_obj.write(text_obj)
    obj_to_stl('data/bunny_short.obj', 'data/bunny_short.stl', 'bunny_short')
    mo.show_code(show("data/bunny_short.stl", scale=1.5))
    return file_obj, text_obj


@app.cell
def __(mo):
    mo.md(
        rf"""
    ## Binary STL

    Since the STL ASCII format can lead to very large files when there is a large number of facets, there is an alternate, binary version of the STL format which is more compact.

    Read about this variant online, then implement the function

    ```python
    def STL_binary_to_text(stl_filename_in, stl_filename_out):
        pass  # 🚧 TODO!
    ```

    that will convert a binary STL file to a ASCII STL file. Make sure that your function works with the binary `data/dragon.stl` file which is an example of STL binary format.

    💡 The `np.fromfile` function may come in handy.

        """
    )
    return


@app.cell
def __(mo, show):
    mo.show_code(show("data/dragon.stl", theta=75.0, phi=-20.0, scale=1.7))
    return


@app.cell
def __(make_STL, np):
    def STL_binary_to_text(stl_filename_in, stl_filename_out):
        with open(stl_filename_in, mode="rb") as file:
            _ = file.read(80)
            n = np.fromfile(file, dtype=np.uint32, count=1)[0]
            normals = []
            faces = []
            for i in range(n):
                normals.append(np.fromfile(file, dtype=np.float32, count=3))
                faces.append(np.fromfile(file, dtype=np.float32, count=9).reshape(3, 3))
                _ = file.read(2)
        text_stl = make_STL(faces, normals)
        with open(stl_filename_out, mode="wt", encoding="utf-8") as file:
            file.write(text_stl)
    return (STL_binary_to_text,)


@app.cell
def __(STL_binary_to_text):
    STL_binary_to_text("data/dragon.stl", "data/dragon_ASCII.stl")
    return


@app.cell
def __(mo, show):
    mo.show_code(show("data/dragon_ASCII.stl", theta=75.0, phi=-20.0, scale=1.7))
    return


@app.cell
def __(mo):
    mo.md(rf"""## Constructive Solid Geometry (CSG)

    Have a look at the documentation of [{mo.icon("mdi:github")}fogleman/sdf](https://github.com/fogleman/) and study the basics. At the very least, make sure that you understand what the code below does:
    """)
    return


@app.cell
def __(X, Y, Z, box, cylinder, mo, show, sphere):
    demo_csg = sphere(1) & box(1.5)
    _c = cylinder(0.5)
    demo_csg = demo_csg - (_c.orient(X) | _c.orient(Y) | _c.orient(Z))
    demo_csg.save('output/demo-csg.stl', step=0.05)
    mo.show_code(show("output/demo-csg.stl", theta=45.0, phi=45.0, scale=1.0))
    return (demo_csg,)


@app.cell
def __(mo):
    mo.md("""ℹ️ **Remark.** The same result can be achieved in a more procedural style, with:""")
    return


@app.cell
def __(
    box,
    cylinder,
    difference,
    intersection,
    mo,
    orient,
    show,
    sphere,
    union,
):
    demo_csg_alt = difference(
        intersection(
            sphere(1),
            box(1.5),
        ),
        union(
            orient(cylinder(0.5), [1.0, 0.0, 0.0]),
            orient(cylinder(0.5), [0.0, 1.0, 0.0]),
            orient(cylinder(0.5), [0.0, 0.0, 1.0]),
        ),
    )
    demo_csg_alt.save("output/demo-csg-alt.stl", step=0.05)
    mo.show_code(show("output/demo-csg-alt.stl", theta=45.0, phi=45.0, scale=1.0))
    return (demo_csg_alt,)


@app.cell
def __(mo):
    mo.md(
        rf"""
    ## JupyterCAD

    [JupyterCAD](https://github.com/jupytercad/JupyterCAD) is an extension of the Jupyter lab for 3D geometry modeling.

      - Use it to create a JCAD model that correspond closely to the `output/demo_csg` model;
    save it as `data/demo_jcad.jcad`.

      - Study the format used to represent JupyterCAD files (💡 you can explore the contents of the previous file, but you may need to create some simpler models to begin with).

      - When you are ready, create a `jcad_to_stl` function that understand enough of the JupyterCAD format to convert `"data/demo_jcad.jcad"` into some corresponding STL file.
    (💡 do not tesselate the JupyterCAD model by yourself, instead use the `sdf` library!)


        """
    )
    return


@app.cell
def __(box, cylinder, difference, intersection, orient, sphere, union):
    def jcad_to_stl(jcad_filename, stl_filename):
        with open(jcad_filename, mode="rt", encoding="utf-8") as file_stl:
            jcad_text = file_stl.read().replace('false', 'False').replace('true', 'True')
        dico = eval(jcad_text)
        Ls = dico['objects']
        dictionnaire = {}   
        for dict in Ls:
            type_objet = dict['shape']
            shape = dict['shape']
            if shape == 'Part::Sphere':
                radius = dict['parameters'].get('Radius')
                dictionnaire[dict['name']] = sphere(radius)
            elif shape == 'Part::Box':
                height = dict['parameters'].get('Height')
                length = dict['parameters'].get('Length')
                width = dict['parameters'].get('Width')
                dictionnaire[dict['name']] = box((height, length, width))
            elif shape == 'Part::Cylinder':
                radius = dict['parameters'].get('Radius')
                axis = dict['parameters']['Placement'].get('Axis')
                dictionnaire[dict['name']] = orient(cylinder(radius), axis=axis)
            elif shape == 'Part::MultiCommon':
                form1 = dict['dependencies'][0]
                form2 = dict['dependencies'][1]
                dictionnaire[dict['name']] = intersection(dictionnaire[form1], dictionnaire[form2])
                operation = dict['name']
            elif shape == 'Part::MultiFuse':
                form1 = dict['dependencies'][0]
                form2 = dict['dependencies'][1]
                dictionnaire[dict['name']] = union(dictionnaire[form1], dictionnaire[form2])
                operation = dict['name']
            elif shape == 'Part::Cut':
                form1 = dict['dependencies'][0]
                form2 = dict['dependencies'][1]
                dictionnaire[dict['name']] = difference(dictionnaire[form1], dictionnaire[form2])
                operation = dict['name']

        demo_csg_alt = dictionnaire[operation]
        demo_csg_alt.save(stl_filename, step=0.05)

    # Pour que notre fonction réalise la tache demandée, il faut que les différentes formes du fichiers jcad soient crées avant les actions (intersection, union,difference) et que ces dernières soient dans le bon ordre.
    return (jcad_to_stl,)


@app.cell
def __(jcad_to_stl):
    jcad_to_stl("data/demo_jcad.jcad", "data/demo_stl.stl")
    return


@app.cell
def __(mo, show):
    mo.show_code(show("data/demo_stl.stl", theta=45.0, phi=45.0, scale=1.0))
    return


@app.cell
def __(mo):
    mo.md("""## Appendix""")
    return


@app.cell
def __(mo):
    mo.md("""### Dependencies""")
    return


@app.cell
def __():
    # Python Standard Library
    import json

    # Marimo
    import marimo as mo

    # Third-Party Librairies
    import numpy as np
    import matplotlib.pyplot as plt
    import mpl3d
    from mpl3d import glm
    from mpl3d.mesh import Mesh
    from mpl3d.camera import Camera

    import meshio

    np.seterr(over="ignore")  # 🩹 deal with a meshio false warning

    import sdf
    from sdf import sphere, box, cylinder
    from sdf import X, Y, Z
    from sdf import intersection, union, orient, difference

    mo.show_code()
    return (
        Camera,
        Mesh,
        X,
        Y,
        Z,
        box,
        cylinder,
        difference,
        glm,
        intersection,
        json,
        meshio,
        mo,
        mpl3d,
        np,
        orient,
        plt,
        sdf,
        sphere,
        union,
    )


@app.cell
def __(mo):
    mo.md(r"""### STL Viewer""")
    return


@app.cell
def __(Camera, Mesh, glm, meshio, mo, plt):
    def show(
        filename,
        theta=0.0,
        phi=0.0,
        scale=1.0,
        colormap="viridis",
        edgecolors=(0, 0, 0, 0.25),
        figsize=(6, 6),
    ):
        fig = plt.figure(figsize=figsize)
        ax = fig.add_axes([0, 0, 1, 1], xlim=[-1, +1], ylim=[-1, +1], aspect=1)
        ax.axis("off")
        camera = Camera("ortho", theta=theta, phi=phi, scale=scale)
        mesh = meshio.read(filename)
        vertices = glm.fit_unit_cube(mesh.points)
        faces = mesh.cells[0].data
        vertices = glm.fit_unit_cube(vertices)
        mesh = Mesh(
            ax,
            camera.transform,
            vertices,
            faces,
            cmap=plt.get_cmap(colormap),
            edgecolors=edgecolors,
        )
        return mo.center(fig)

    mo.show_code()
    return (show,)


@app.cell
def __(mo, show):
    mo.show_code(show("data/teapot.stl", theta=45.0, phi=30.0, scale=2))
    return


if __name__ == "__main__":
    app.run()
