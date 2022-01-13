# Multi-Objective Green Supply Chain Optimizat

<h2>1. Background and Motivation </h2>

### 1.1 Background:
Green Supply Chain refers to the management between the **facility operation, transportation and environmental effects of all facilities in a supply chain**, i.e. the environment protection constraint is brought into facility location and allocation. Its purpose is to add environment protection consciousness into production and transportation, in order to improve the competitive edge of the supply chain regarding environmental effects.

### 1.2 Motivation:
The aim of most supply chain optimization problems is to minimize the total cost of the supply chain. However, since environmental protection is of concern to the public, a green supply chain,because of its minimum effect on nature, has been seriously considered as a solution to this concern.

### 1.3 Problem Definition:
We want to **minimize the total cost** of the supply chain and **minimize the air pollution discharged from the supply chain** to reduce the impact on the environment.

<h2>2.Green Supply Chain Model(SCM) </h2>
There are some important roles in a supply chian:

1.Manufacturers  
2.Warehouses  
3.Distribution centers  
4.Customers  

And these four roles will have the following five activities:

1.Purchase raw materials from Manufacturer   
2.Assemble products in Manufacturers  
3.Transport products from Manufacturers to Warehouses  
4.Transport products from Warehouses to Distribution centers  
5.Transport products from Distribution centers to customers


We assume **3 Manufacturers,4 Warehouses,5 Distribution centers,16 Customers**,below figure is an  assumption example which shows the structure of a supply chain:

![擷取](https://user-images.githubusercontent.com/51538779/149259852-8f6f8a11-9375-4788-a22e-24818ea20363.JPG)



Notations of SCM
The notations of SCM are as following table

<table>
<tr>
<th>Set</th> <th>Description</th> 
</tr>
<tr>
<th>C</th> <th>customers</th> 
</tr>
<tr>
<th>D</th> <th>distribution centers</th> 
</tr>
<tr>
<th>W</th> <th>warehouses</th>
</tr>
<tr>
<th>M</th> <th>manufacturers</th>
</tr>
<tr>
<th>TM</th> <th>transportation options for manufacturers</th>
</tr>
<tr>
<th>TW</th> <th>transportation options for warehouses</th>
</tr>
<tr>
<th>TD</th> <th>transportation options for distribution centers</th>
</tr>
<tr>
<th>I</th> <th>suppliers producing raw material, type i</th>
</tr>
<tr>
<th>J</th> <th> suppliers producing raw material, type j</th>
</tr>
</table>

-------------------------

![messageImage_1642046021182](https://user-images.githubusercontent.com/51538779/149263199-1be752bc-9c1e-4607-9b0d-f3399d45041f.jpg)

<table>
 <tr><th>Parameter</th> <th>Description</th> </tr>
 <tr><th>dem<sub>c</sub> </th><th>demand of customer c with mean μc and standard deviation σc</th></tr>
 <tr><th>dem<sub>f</sub> </th><th>demand of facility f ∈ {m,w, d} </th></tr>
 <tr><th>cr<sup>i</sup><sub>m</sub> </th><th>unit raw material cost from supplier of type i to manufacturer m </th></tr>
 <tr><th>cr<sup>j</sup><sub>m</sub> </th><th>unit raw material cost from supplier of type j to manufacturer m </th></tr>
 <tr><th>c<sup>tm</sup><sub>mw</sub> </th><th>unit transportation cost from manufacturer m to warehouse w with transportation option tm</th></tr>
  <tr><th>c<sup>tw</sup><sub>wd</sub> </th><th>unit transportation cost from warehouse w to distribution centers d  with transportation option tw</th></tr>
 <tr><th>c<sup>td</sup><sub>dc</sub> </th><th>unit transportation cost from distribution center d tocustomer c with transportation option td</th></tr>
  <tr><th>dis<sub>ff′</sub> </th><th>distance between facility f ∈ {m,w, d} and facility f ′ ∈ {w, d, c} </th></tr>
 <tr><th>fc<sub>f</sub> </th><th>fixed cost of opening facility f ∈ {m,w, d}</th></tr>
  <tr><th>lt<sub>m</sub> </th><th>lead time of facility f ∈ {m,w}</th></tr>
 <tr><th>vc<sub>f</sub> </th><th>unit variable cost per unit for facility f ∈ {m,w, d}</th></tr>
  <tr><th>inv<sub>f</sub> </th><th>expected inventory at facility f ∈ {w, d}</th></tr>
 <tr><th>nrr<sup>i</sup> </th><th>number of units of raw material of type i required to produce one unit of the product</th></tr>
  <tr><th>nrr<sup>j</sup> </th><th>number of units of raw material of type j required to produce one unit of the product</th></tr>
  <tr><th>p</th><th>penalty cost per unit of customer demand if it is not fulfilled</th></tr>
 <tr><th>ca<sub>f</sub> </th><th>the capacity of facility f ∈ {m,w, d}</th></tr>
 <tr><th>ca<sup>f′</sup> </th><th>capacity of transportation option f ′ ∈ {tm, tw, td}</th></tr>
  <tr><th>G<sup>f</sup><sub>N</sub> </th><th>rate of released nitrogen oxide to produce/handle one unit of product in facility f ∈ {m,w, d}</th></tr>
 <tr><th>G<sup>f</sup><sub>C</sub> </th><th>rate of released carbon monoxide to produce/handle one unit of product in facility f ∈ {m,w, d}</th></tr>
 <tr><th>G<sup>f</sup><sub>O</sub> </th><th>rate of released organic to produce/handle one unit of product in facility f ∈ {m,w, d}</th></tr>
 <tr><th>G<sup>f′</sup><sub>N</sub> </th><th>rate of released nitrogen oxide per one unit of distance for transportation option f ′ ∈ {tm, tw, td}</th></tr>
 <tr><th>G<sup>f′</sup><sub>C</sub> </th><th>rate of released carbon monoxide per one unit of distance for transportation option f ′ ∈ {tm, tw, td}</th></tr>
 <tr><th>G<sup>f′</sup><sub>O</sub> </th><th>rate of released volatile organic per one unit of distance for transportation option f ′ ∈ {tm, tw, td}</th></tr>
 
 </table>
 
