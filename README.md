Blockchain fraud detection: Let’s analyze the data!
(In progress due 06/20/2021)

Emily Bauer(emmit.bauer@gmail.com)
Kyusub Hwang (kyusubhwang@hanyang.ac.kr)

Contents

1.	basic mechanism of blockchain.
2.	hash algorithm
3.	blockchain fraud detection
•	possible weakness of blockchain (restricted amount of transactions, mining issues, address issues, etcs … )
•	previous incidents on blockchain fraud (in year 2016, whole transactions in a block disappeared due to wrong wallet address settings)
•	solution; How to prevent it?
4.	analysis on the bitcoin transactions in the given json. 
•	how many transactions/unique wallet addresses there are w/ graphs + charts.
5.	demonstration of ‘Block’ ‘Chain’ 
•	showing interconnections between Blocks using hash values

6.	Conclusion

Body 

1. Basic mechanism of blockchain (with some info about Bitcoin)

The most well-known application of blockchain technology is Bitcoin, the leading cryptocurrency. The major security behind Bitcoin is based around the use of blockchain technology, so it is an imperative feature. Before understanding Bitcoin, and other blockchain transactions, the basic mechanisms of blockchain must be explained. The base of a blockchain is a single block. “In its simplest form, a block is an encrypted aggregation of a set of transactions.” (4) So, in the case of Bitcoin transactions, the blockchain is able to represent a complete, decentralized ledger of transaction history in an encrypted format that makes fraudulently changing the ledger quite difficult (1). Each computer in the network has a copy of the ledger. Thus, if a change is made, every copy will be updated.

A blockchain, as the name suggests, is similar to a linked list where each block references the previous block through the use of its hash. The block also contains the hash of its own contents (4). Thus, changing the contents of any one block would alter the hash of that block, meaning that the reference to that block would be altered in the next block, and so on. This means that all subsequent blocks in the chain will also be altered, invalidating them.

An authentic Bitcoin transaction requires a set of public and private keys that are used as a digital signature to verify the transaction (6). The network can then confirm that this transaction is valid, using information about previous transactions, and the transaction can be written to a block (6). However, writing to a block is not a straightforward process. The only way to effectively alter a block is to alter that block and all the subsequent blocks, which requires a lot of work (5). This work comes from the process needed to validate a block within the blockchain. “…Bitcoin makes it computationally difficult to hash a block, by requiring that the resulting hash have specific numeric properties.” (7) This is known as proof of work. More specifically, in order to validate the block, a special number called a nonce must be found via random guessing. The correct nonce inserted into the hash function will create a certain desired hash value, usually ones starting with a certain number of zeros. Finding the correct nonce takes quite a bit of computational work, as well as time. Thus, having to do this multiple times, once for every block affected by changing the blockchain, becomes a nearly infeasible task.

![image](https://user-images.githubusercontent.com/79511478/120931171-74adcb00-c72b-11eb-84b1-99b1dc55258f.png)

(9)

(1) https://link.springer.com/content/pdf/10.1007/s12599-017-0467-3.pdf
(4) https://www.researchgate.net/profile/Suyash-Gupta-5/publication/325116198_Blockchain_Transaction_Processing/links/5af8c85f4585157136ec1bc0/Blockchain-Transaction-Processing.pdf
(5) https://hal.archives-ouvertes.fr/hal-01716687v2/document
(6) https://digitalcommons.bryant.edu/cisjou/28/
(7) https://www.sciencedirect.com/science/article/pii/S1361372313701015?casa_token=2KsbcVcWZz0AAAAA:G-POctQ0chtx1Rw_U3AEm1l3WbXMuQmD1FxOoS0pCzBzcyagptGdXvHwDZvURGi5uWDAdU5qrPLD
(9) https://j2-capital.com/wp-content/uploads/2017/11/AIR-2016-Blockchain.pdf



2. Hash function
What is Hash Function?
Hash function is a mathematical algorithm that produces output which cannot be traced back to its input.
-       It is deterministic; same output is guaranteed from the same input.
-       It is irreversible; cannot reverse output back to its input. (pre-image)
-       It is regular; fixed size of output is returned from arbitrary size of input
-       It is obscure; small change of input dramatically affects its output. (avalanche effect)
-       It is unique; computationally cannot find another input which produces the same output. (collision-resistance)
 
Cryptographic Hash Functions
 Secure Hash Algorithms (SHA) are a family of cryptographic hash functions published by the National Institute of Standards and Technology (NIST) as a U.S. Federal Information Processing Standard (FIPS). There are various versions of SHA, and SHA-256 is one of the most broadly used in blockchain protocols. Along with other multiple coins, Bitcoin uses SHA-256 hashing algorithm.
 
Comparison of SHA
![image](https://user-images.githubusercontent.com/79511478/120931459-8e034700-c72c-11eb-87e8-ce4e495187ad.png)
 
SHA-2 Mechanism
 ![image](https://user-images.githubusercontent.com/79511478/120931186-81322380-c72b-11eb-882f-b501fe502417.png)

*Wikipedia (https://en.wikipedia.org/wiki/SHA-2)

 SHA-256 is a newer, more secure cryptographic hash function which was proposed in 2000 as a new generation of SHA functions and was adopted as FIPS standard in 2002. The SHA-256 algorithm generates a 256-bit hash value from padded 512-bit message blocks, and the original message size is up to 264-1 bits. SHA-256 always computes a 256-bit hash internally for security, but this resulting can be truncated to either 196 or 128 bits printing and storage. Thus a truncated SHA-256 yields a substantial benefit for human usability in printed citations, and significantly improves security, at the cost of a small reduction in performance related to MD5. Unlike the MD5 algorithm, truncated SHA-256 is not subject to any known attacks.

*source: http://www.differencebetween.net/technology/difference-between-sha-256-and-sha-1/#ixzz6wY4odRtm

3. Blockchain Fraud Detection
Possible weaknesses: 
•	scalability: “the number of transactions that could be handled per second is extremely low when compared to traditional systems.” “Apart from time, space is also an issue, since data are replicated on each network node. To make an example, the Bitcoin blockchain requires more than 170 GB of storage on each network node.”
•	privacy: “once information is encoded in the blockchain, it is immutable and accessible by everyone is another weakness, and could harm users’ privacy.”
•	relatively new: “development tools are still in an early stage, and standards for developing blockchain-based applications have not been defined yet.”

Source: https://www.mdpi.com/1999-5903/10/2/20/htm 

Previous incidents on blockchain fraud:
•	


4. Block Analysis
 
Each block consists of two parts: Header and Body.
![image](https://user-images.githubusercontent.com/79511478/120931190-88593180-c72b-11eb-9b57-2dff32778b56.png)

*source:https://www.researchgate.net/figure/The-structure-of-a-Blockchain-A-block-is-composed-of-a-header-and-a-body-where-a-header_fig1_337306138

![image](https://user-images.githubusercontent.com/79511478/120931196-8becb880-c72b-11eb-9e37-4c17c7fefe03.png)
 
Due to heavy size of the given json, it was impossible/inefficient to load the whole data with limited computing resources. I used ijson python library to read and analyze the json line by line.
(You can also view it from here: https://blockchain.info/block-height/556459?format=json)

 ![image](https://user-images.githubusercontent.com/79511478/120931203-914a0300-c72b-11eb-9dfc-a72e133a7c6f.png)

As mentioned above, we can easily check that this block does consist of header and body information.
(terminology explanation will be updated)
merkleroot :
nonce :
previousblockhash :
hash :
version :
weight :
nTx :
chainwork :
~
strippedsize :

 
 ![image](https://user-images.githubusercontent.com/79511478/120931209-93ac5d00-c72b-11eb-8f96-0b96b2c0ff0d.png)

Among header information, what we need to verify the block’s integrity are version, previousblockhash, merkleroot, time, bits, nonce.
After parsing appropriately and applying double SHA-256 hashing algorithm, then we can verify that the block’s header information is correct because any small frauds of the block will result in unpredictable hash values (avalanche effect).
 ![image](https://user-images.githubusercontent.com/79511478/120931223-9c049800-c72b-11eb-9b08-bfa938128558.png)

Blockchain Hash Calculator using double SHA-256
•	Block Transaction Fraud Detector can be generated by checking merkleroot’s each nodes’ hash values, probably using LRV tree traversing algorithm. 
 ![image](https://user-images.githubusercontent.com/79511478/120931237-a030b580-c72b-11eb-9ced-460252fb6869.png)

* source : https://decentralizedthoughts.github.io/2020-12-22-what-is-a-merkle-tree/ 


Conclusion
- TBD

	Source
•	https://www.youtube.com/watch?v=_160oMzblY8&ab_channel=AndersBrownworthAndersBrownworth
•	https://en.bitcoin.it/wiki/Transaction
•	https://en.bitcoin.it/wiki/Protocol_rules#.22tx.22_messages
•	https://en.bitcoin.it/wiki/Protocol_documentation#BlockTransactions
•	

