# Razor
A restriction enzyme explorer for DNA sequence analysis

# Introduction:
Razor is a tool that quickly scans a DNA nucleotide sequence looking for one-cut restriction enzymes. These restriction enzymes will cut the DNA exacty once (in one spot) and will leave two strands behind (left and right). Once restriction enzyme sites are found, the tool can explore the cuts made by selected enzymes.

# Requirements:
- Python 3.6.1 or greater
- A text file containing the uppercase DNA nucleotides of a 5' to 3' DNA strand (the file dnatest.txt provided is an example of this)

<table>
<tbody><tr>
<th>Symbol<sup id="cite_ref-iupac_2-0" class="reference"><a href="#cite_note-iupac-2">&#91;2&#93;</a></sup></th>
<th>Description</th>
<th colspan="5">Bases represented</th>
<th>Complement
</th></tr>
<tr>
<td><b>A</b></td>
<td align="left"><a href="/wiki/Adenine" title="Adenine"><b>A</b>denine</a></td>
<td>A</td>
<td></td>
<td></td>
<td></td>
<td rowspan="5">1</td>
<td>T
</td></tr>
<tr>
<td><b>C</b></td>
<td align="left"><a href="/wiki/Cytosine" title="Cytosine"><b>C</b>ytosine</a></td>
<td></td>
<td>C</td>
<td></td>
<td></td>
<td>G
</td></tr>
<tr>
<td><b>G</b></td>
<td align="left"><a href="/wiki/Guanine" title="Guanine"><b>G</b>uanine</a></td>
<td></td>
<td></td>
<td>G</td>
<td></td>
<td>C
</td></tr>
<tr>
<td><b>T</b></td>
<td align="left"><a href="/wiki/Thymine" title="Thymine"><b>T</b>hymine</a></td>
<td></td>
<td></td>
<td></td>
<td>T</td>
<td>A
</td></tr>
<tr>
<td><b>U</b></td>
<td align="left"><a href="/wiki/Uracil" title="Uracil"><b>U</b>racil</a></td>
<td></td>
<td></td>
<td></td>
<td>U</td>
<td>A
</td></tr>
<tr bgcolor="#e8e8e8">
<td><b>W</b></td>
<td align="left"><b>W</b>eak</td>
<td>A</td>
<td></td>
<td></td>
<td>T</td>
<td rowspan="6">2</td>
<td>W
</td></tr>
<tr bgcolor="#e8e8e8">
<td><b>S</b></td>
<td align="left"><b>S</b>trong</td>
<td></td>
<td>C</td>
<td>G</td>
<td></td>
<td>S
</td></tr>
<tr bgcolor="#e8e8e8">
<td><b>M</b></td>
<td align="left"><a href="/wiki/Amine" title="Amine">a<b>M</b>ino</a></td>
<td>A</td>
<td>C</td>
<td></td>
<td></td>
<td>K
</td></tr>
<tr bgcolor="#e8e8e8">
<td><b>K</b></td>
<td align="left"><a href="/wiki/Ketone" title="Ketone"><b>K</b>eto</a></td>
<td></td>
<td></td>
<td>G</td>
<td>T</td>
<td>M
</td></tr>
<tr bgcolor="#e8e8e8">
<td><b>R</b></td>
<td align="left"><a href="/wiki/Purine" title="Purine">pu<b>R</b>ine</a></td>
<td>A</td>
<td></td>
<td>G</td>
<td></td>
<td>Y
</td></tr>
<tr bgcolor="#e8e8e8">
<td><b>Y</b></td>
<td align="left"><a href="/wiki/Pyrimidine" title="Pyrimidine">p<b>Y</b>rimidine</a></td>
<td></td>
<td>C</td>
<td></td>
<td>T</td>
<td>R
</td></tr>
<tr>
<td><b>B</b></td>
<td align="left">not A (<b>B</b> comes after A)</td>
<td></td>
<td>C</td>
<td>G</td>
<td>T</td>
<td rowspan="4">3</td>
<td>V
</td></tr>
<tr>
<td><b>D</b></td>
<td align="left">not C (<b>D</b> comes after C)</td>
<td>A</td>
<td></td>
<td>G</td>
<td>T</td>
<td>H
</td></tr>
<tr>
<td><b>H</b></td>
<td align="left">not G (<b>H</b> comes after G)</td>
<td>A</td>
<td>C</td>
<td></td>
<td>T</td>
<td>D
</td></tr>
<tr>
<td><b>V</b></td>
<td align="left">not T (<b>V</b> comes after T and U)</td>
<td>A</td>
<td>C</td>
<td>G</td>
<td></td>
<td>B
</td></tr>
<tr bgcolor="#e8e8e8">
<td><b>N</b></td>
<td align="left">any <b>N</b>ucleotide (not a gap)</td>
<td>A</td>
<td>C</td>
<td>G</td>
<td>T</td>
<td>4</td>
<td>N
</td></tr>
<tr>
<td><b>Z</b></td>
<td align="left"><a href="/wiki/0" title="0"><b>Z</b>ero</a></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>0</td>
<td>Z
</td></tr></tbody></table>

# Commands:
We are using python 3 so each command begins with 'python3'. This may be 'python' or 'python3' on your system but hopeully you will be able to figure this out! After CDing into the directory where these project files are:

- For a list of commands type: ```python3 main.py```
- To use the analyze function type: ```python3 main.py --analyze dnatest.txt```
- To use the cut function type: ```python3 main.py --cut dnatest.txt <enzyme name copied from analysis list>```
- To use the search function type: ```python3 --search dnatest.py <sequence to search for>```
  
![alt text](https://i.ibb.co/vB7rrSw/Doc1.png)

To use the makereport function type: ```python3 main.py --makereport dnatest.py```

![alt text](https://i.ibb.co/TW58xk2/doc2.png)

which outputs a text file structured as the following with name dnatest_report.txt

![alt text](https://i.ibb.co/njrtyNn/doc3.png)
