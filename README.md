# Razor
A restriction enzyme explorer for DNA sequence analysis

# Introduction:
Razor is a tool that quickly scans a DNA nucleotide sequence looking for one-cut restriction enzymes. These restriction enzymes will cut the DNA exacty once (in one spot) and will leave two strands behind (left and right). Once restriction enzyme sites are found, the tool can explore the cuts made by selected enzymes.

# Requirements:
- Python 3.6.1 or greater
- A text file containing the uppercase DNA nucleotides of a 5' to 3' DNA strand (the file dnatest.txt provided is an example of this)

<table>
      <tbody>
            <tr>
             <td bgcolor="#88FF88" valign="top"><center>
             A<br />             
             </center></td>
             <td bgcolor="#88FF88" valign="top"><center>
             Adenine
             </center></td>
             <td bgcolor="#88FF88" valign="top"><center>
             T<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#88FF88" valign="top"><center>
             G<br />             
             </center></td>
             <td bgcolor="#88FF88" valign="top"><center>
             Guanine
             </center></td>
             <td bgcolor="#88FF88" valign="top"><center>
             C<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#88FF88" valign="top"><center>
             C<br />             
             </center></td>
             <td bgcolor="#88FF88" valign="top"><center>
             Cytosine
             </center></td>
             <td bgcolor="#88FF88" valign="top"><center>
             G<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#88FF88" valign="top"><center>
             T<br />             
             </center></td>
             <td bgcolor="#88FF88" valign="top"><center>
             Thymine
             </center></td>
             <td bgcolor="#88FF88" valign="top"><center>
             A<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFFF99" valign="top"><center>
             Y<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
              Pyrimidine (C or T)<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
             R<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFFF99" valign="top"><center>
             R<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
              Purine (A or G)<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
             Y<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFFF99" valign="top"><center>
             W<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
              weak (A or T)<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
             W<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFFF99" valign="top"><center>
             S<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
              strong (G or C)<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
             S<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFFF99" valign="top"><center>
             K<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
              keto (T or G)<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
             M<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFFF99" valign="top"><center>
             M<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
              amino (C or A)<br />             
             </center></td>
             <td bgcolor="#FFFF99" valign="top"><center>
             K<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFBA75" valign="top"><center>
             D<br />             
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             A, G, T (not C)<br />             
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             H<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFBA75" valign="top"><center>
             V<br />             
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             A, C, G (not T)<br />             
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             B<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFBA75" valign="top"><center>
             H<br />             
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             A, C, T (not G)<br />             
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             D<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFBA75" valign="top"><center>
             B<br />             
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             C, G, T (not A)<br />             
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             V<br />             
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFBA75" valign="top"><center>
             X/N
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             any base 
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             X/N
             </center></td>
            </tr>
            <tr>
             <td bgcolor="#FFBA75" valign="top"><center>
             -<br />             
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             Gap<br />             
             </center></td>
             <td bgcolor="#FFBA75" valign="top"><center>
             -<br />             
             </center></td>
            </tr>
</tbody>
</table>


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
