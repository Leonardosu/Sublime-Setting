# Personal Sublime Text Settings

## Sublime packages:
### CMD:
    - Key bind:
        alt + c, alt + d
    - Open cmd on current file path
### User:
    Snippet, build and key binds.
    - build1:
        type "zt" to write c++ template with many cases tests.
    - build2:
        type "zz" to write c++ template with one case test.
    - Default (Windows):
        set of key binds

    To use a Snippet, type a key-word on c++ file and press tab, e.g: "zfft"
    * All Snippet has "z" prefix
    - Fast Fourier Transform:
        "zfft"
    - Fast Fourier Transform with modulo:
        "zfftMod"
    - Gcd (Greatest Common Divisor):
        "zgcd"
    - Modular Inverse for the first N numbers:
        "zinvMod"
    - Number Theoretic Transform:
        "zntt"
    - Palindrome Tree:
        "zPalinTree"
    - Binary exponentiation:
        "zpoww"
    - Dynamic/Implicit/Sparse  Segment Tree:
        "zSegtreeDinamica"
    - Trie:
        "ztrie"
    - Two Sat:
        "ztwoSat"
    - Union Find:
        "zzUnionFind"

## Create a cmd Macro:
Macro to run a python script that make a folder with _n_  C++ files.

1. Make path C:\bat\
2. Create the file "macros.doskey" and write: "gen=python3 python_file_name.py $1 $2"
3. Type in cmd:
    -   reg add "HKCU\Software\Microsoft\Command Processor" /v Autorun /d "doskey /macrofile=\"C:\bat\macros.doskey\"" /f
    -   reg query "HKCU\Software\Microsoft\Command Processor" /v Autorun


