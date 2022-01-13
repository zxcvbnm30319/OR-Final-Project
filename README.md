# Multi-Objective Green Supply Chain Optimization

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

### Sets:
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
### Notation:
![messageImage_1642046021182](https://user-images.githubusercontent.com/51538779/149263199-1be752bc-9c1e-4607-9b0d-f3399d45041f.jpg)

### Parameter:
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
 
 ### Decision Variables:
 <table>
  <tr><th>Decision Variables</th><th>Description</th></tr>
  <tr><th>x<sub>m</sub> </th><th>1 if manufacturer m is opened  / 0 otherwise</th></tr>
 <tr><th>x<sub>w</sub> </th><th>1 if warehouse w is opened  / 0 otherwise</th></tr>
 <tr><th>x<sub>d</sub> </th><th>1 if distribution house d is opened  / 0 otherwise</th></tr>
 <tr><th>x<sup>tm</sup><sub>mw</sub></th><th>quantity of products shipped from manufacturer m to warehouse w by transportation option tm</th></tr>
 <tr><th>x<sup>tw</sup><sub>wd</sub></th><th>quantity of products shipped from warehouse w to distribution center d by transportation option tw</th></tr>
  <tr><th>x<sup>td</sup><sub>dc</sub></th><th>quantity of products shipped from distribution center d tocustomer c by transportation option td</th></tr>
 <tr><th>x<sup>i</sup><sub>m</sub></th><th>quantity of raw material transported to manufacturer m from supplier that produce raw material type i</th></tr>
 <tr><th>x<sup>j</sup><sub>m</sub></th><th>quantity of raw material transported to manufacturer m from supplier that produce raw material type j</th></tr>
 </table>

 ### Objective function:
 
* **Objective function 1 --> Minimize cost:**

![1](https://user-images.githubusercontent.com/51538779/149276126-295e3e96-ffd7-4801-9895-254bb983b53d.JPG)

* **Objective function 2 --> Minimize pollution:**

![2](https://user-images.githubusercontent.com/51538779/149276436-741e0180-dff0-423d-a26d-2e58a0c9fd0f.JPG)


 ### Constraints:

(12)–(14) determine the demand of each facility:  
![12](https://user-images.githubusercontent.com/51538779/149278103-8afbba16-fee2-4f5d-9084-893b1614977a.JPG)


(15) and (16) also calculate the inventory level that each warehouse and distribution center must hold:  
![15](https://user-images.githubusercontent.com/51538779/149278113-b75d1b00-3b49-4b21-b18f-90413f675095.JPG)


(17)–(18) also show that the standard deviation of demand for warehouses and distribution centers is defined as the weighted average of the standard deviation of demands assigned to them:  
![17](https://user-images.githubusercontent.com/51538779/149278123-303c3105-ebeb-4967-b0c0-1d0de0ff9a16.JPG)


(19)–(21) ensure that we cannot assign a demand to a facility that is higher than its capacity:  
![19](https://user-images.githubusercontent.com/51538779/149277379-b099d20a-faef-49e1-9b49-bd719e2c6bf0.JPG)

(22)–(24) assure that if a facility does not supply any facility at its lower level, it will be closed and its binary variable is equal to zero:  
![22](https://user-images.githubusercontent.com/51538779/149277514-8e2613e7-b83d-4809-9ed6-72da17b77e5c.JPG)

(25) and (26) guarantee that the total raw material shipped from suppliers to a manufacturer can not be greater than the manufacturer demand, according to the required raw material for one product unit:  
![25](https://user-images.githubusercontent.com/51538779/149277624-0b17ea65-a632-4a8f-8baa-9c5c84cce3de.JPG)

(27)–(28) ensure that the amount of product transported from a manufacturer and a warehouse must be equal to warehouse and distribution center demand respectively:  
![27](https://user-images.githubusercontent.com/51538779/149277831-cb22e368-8085-4e79-981b-54bdf18bbb42.JPG)

(29) distribution centers are allowed to not serve the percentage or total demand of a customer:  
![29](https://user-images.githubusercontent.com/51538779/149277896-eae91369-e110-4407-a757-794893801822.JPG)

(30)–(32) are capacity constraints on transportation means, which prohibit assigning more than their capacity to the transportation means:  
![30](https://user-images.githubusercontent.com/51538779/149277933-6709eedb-8b82-444e-86b0-c95de1d6ba14.JPG)


<h2>3. Methodology </h2>

### ϵ-constrained method
We minimize two objectives by setting one objectives to the constraint.
![圖片5](https://user-images.githubusercontent.com/51538779/149279369-435e33c6-e036-4840-9c98-78bf93665b2b.png)  
![擷取000](https://user-images.githubusercontent.com/51538779/149279772-43b65175-1c24-4260-b3ae-a749ba645bb0.JPG)

This is a **nonlinear problem** because  subtitute (17)(18) into (15)(16). We call a module from Python,called **"Pyomo"**.  
There is a solver **Ipopt**  can caculate continuous nonlinear problems.
![P](https://user-images.githubusercontent.com/51538779/149280809-0e37d5eb-edfd-4c01-a957-376020bc530c.JPG)


<h2> 4.Analysis Result </h2>


### 4.1 Analyze the different nubmber of manufacturer and distribution center
Both the nubmber of manufacturer and distribution center increase,the cost and pollution are also increased in SCM.  
However,the distribution center has many routes, when the number of distribution centers increases, the cost and pollution increase is larger than that of the manufacturer.
![AAA1111](https://user-images.githubusercontent.com/51538779/149289120-21d00f06-8ddb-4ccc-a9ae-bb9e332dacf2.JPG)



### 4.2 Analyze the different nubmber of customers
The following pictures show that transportation cost account for large proportion in SCM.  
If the customer number grow ,more products could not deliverd to customer in time so that the backorder cost increase. 
![CCC](https://user-images.githubusercontent.com/51538779/149283068-6062660d-9672-4f6f-a503-cc8efca36d89.JPG)

### 4.3 Analyze the different nubmber of customers

