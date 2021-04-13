# AHPtableGenerator
Simple interactive Python script that generate a Analitic Hierarchy Process table, it exports a .tex code file and a .pdf file.

## Requirements
1. LaTeX installed<br/>
`sudo apt-get install texlive-full`
2. Python 3.6 installed<br/>
`python3 -V`
4. numpy package<br/>
`pip install numpy`
4. PyLaTeX package<br/>
`pip install pylatex`

## Installation
`git clone https://github.com/hasecilu/AHPtableGenerator.git`<br/>

## Usage
1. Open the folder via terminal<br/>
`cd AHPtableGenerator`<br/>
2. Run the script via terminal<br/>
`python3 AHPtableGenerator.py`<br/>
3. Follow the instructions in the terminal
4. Modify the .tex file if needed it and add it to your document

## Example of generated file
![Example1](https://raw.github.com/hasecilu/AHPtableGenerator/master/images/example1.png)
## Example of generated file with manual modifications
Change `\hline` to `\toprule`, `\midrule` and`\bottomrule` in LaTeX file.<br/>
Example of table code after some modifications
```latex
\usepackage{booktabs} % Add this line to the preamble (before \begin{document})

\begin{table}[!ht]
	\centering
	\begin{tabular}{ccccccc}
		\toprule
		Criterios &   R    &   G    &   B    &   W    & Total de fila & Vector de prioridad \\ \midrule
		    R     & 0.0769 & 0.0345 & 0.1053 & 0.0704 &    0.2871     &    {[}0.0718{]}     \\
		    G     & 0.1538 & 0.069  & 0.0526 & 0.0845 &    0.3599     &     {[}0.09{]}      \\
		    B     & 0.3077 & 0.5517 & 0.4211 & 0.4225 &     1.703     &    {[}0.4258{]}     \\
		    W     & 0.4615 & 0.3448 & 0.4211 & 0.4225 &    1.6499     &    {[}0.4125{]}     \\ \midrule
		  Suma    & 0.9999 &  1.0   & 1.0001 & 0.9999 &    3.9999     &    {[}1.0001{]}     \\ \bottomrule
	\end{tabular}
	\caption{Table caption}
\end{table}
```
![Example2](https://raw.github.com/hasecilu/AHPtableGenerator/master/images/example2.png)
