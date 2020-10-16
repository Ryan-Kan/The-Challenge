![The-Challenge Cover Image](https://user-images.githubusercontent.com/25820201/93889162-7493a980-fd1b-11ea-98d9-c6604751ab25.png)

<p align="center">
    <b>The Challenge</b>: A gauntlet of 14 mathematics questions that are to be solved within 15 minutes.
</p>

## What is The Challenge?
The Challenge is a web app which creates 14 mathematics questions which is to be solved within 15 minutes, whilst the tune of [Edvard Grieg's Peer Gynt Suite No. 1, Op. 46](https://en.wikipedia.org/wiki/Peer_Gynt_(Grieg)#Suite_No._1,_Op._46) plays in the background.

The 14 questions will test on different aspects of mathematics, ranging from simple arithmetic to algebra to logarithms to basic calculus.

## Installation
### A. Installing It Pre-Built (Production Server)
1. Navigate to [this folder](dist) (`dist`) that is in the root directory.
2. Download the `.tar.gz` file that is in that folder. (e.g. `The-Challenge-Production-Server_1.0.0a0.dev0.tar.gz`)
3. Extract the contents of that `.tar.gz` file.
4. Follow the instructions of `Production Server Installation Instructions.txt` which can be found in the extracted contents of the `.tar.gz` file.

### B. Building From Source (Development Server)
1. Download the whole repository as a `.zip` file.
    * You can do so by clicking [this link](https://github.com/Ryan-Kan/The-Challenge/archive/master.zip)
2. Extract the contents of that `.zip` file.
3. Navigate to the root directory of The Challenge:
    ```
    cd PATH/TO/ROOT/DIRECTORY
    ```
4. **(Optional)** You may choose to use a virtual environment to install the dependencies of The Challenge.
    * On Ubuntu/Linux, before creating the virtual environment, you may need to run:
        ```
        sudo apt-get install python3-venv
        ```
    * Create a virtual environment (`venv`) using the following command:
        ```
        python3 -m venv venv --prompt NAME_OF_VIRTUAL_ENV
        ```
5. Install all dependencies of The Challenge by running:
    ```
    pip3 install -r requirements.txt
    ```
6. You may run a **development** server by executing the file `the_challenge/__init__.py` or by running the command:
    ```
    python3 the_challenge/__init__.py
    ```

## License
This project is licensed under the MIT license.

The licenses of the software used can be found in the [`licenses.html`](the_challenge/templates/index/licenses.html) file.
