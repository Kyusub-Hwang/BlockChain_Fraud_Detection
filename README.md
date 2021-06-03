# Blockchain fraud detection: Let’s analyze the data! (In progress)

Emily Bauer(emmit.bauer@gmail.com)
Kyusub Hwang (kyusubhwang@hanyang.ac.kr)

Instructions 

- Survey on previous techniques on blockchain transaction analysis
- Dataset is provided (json): all bitcoin transaction records in Jan. 2019.
Available at http://young.hanyang.ac.kr/info/coin.tar.gz
- Possible outline of your work:
o What are the previous incidents on blockchain transaction fraud?
o What are the existing tools (open-source and company) out there?
o Explain how to handle a large dataset.
o Explain what each field means in the data set.
o How many transactions? How many unique wallet addresses? Tables and
graphs are desirable.
o Provide your script or code if possible.
o Any meaningful results that you want to highlight?
o Python, matplotlib, pandas, gnuplot, and etc.


Contents

basic mechanism of blockchain.
hash algorithm
blockchain fraud detection
possible weakness of blockchain (restricted amount of transactions, mining issues, address issues, etcs … )
previous incidents on blockchain fraud (in year 2016, whole transactions in a block disappeared due to wrong wallet address settings)
solution; How to prevent it?
analysis on the bitcoin transactions in the given json. 
how many transactions/unique wallet addresses there are w/ graphs + charts.
demonstration of ‘Block’ ‘Chain’ 
showing interconnections between Blocks using hash values

Conclusion





1. Basic mechanism of blockchain (with some info about Bitcoin)

The most well-known application of blockchain technology is Bitcoin, the leading cryptocurrency. The major security behind Bitcoin is based around the use of blockchain technology, so it is an imperative feature. Before understanding Bitcoin, and other blockchain transactions, the basic mechanisms of blockchain must be explained. The base of a blockchain is a single block. “In its simplest form, a block is an encrypted aggregation of a set of transactions.” (4) So, in the case of Bitcoin transactions, the blockchain is able to represent a complete, decentralized ledger of transaction history in an encrypted format that makes fraudulently changing the ledger quite difficult (1).
Each computer in the network has a copy of the ledger. Thus, if a change is made, every copy will be updated.
A blockchain, as the name suggests, is similar to a linked list where each block references the previous block through the use of its hash. The block also contains the hash of its own contents (4). Thus, changing the contents of any one block would alter the hash of that block, meaning that the reference to that block would be altered in the next block, and so on. This means that all subsequent blocks in the chain will also be altered, invalidating them.
An authentic Bitcoin transaction requires a set of public and private keys that are used as a digital signature to verify the transaction (6). The network can then confirm that this transaction is valid, using information about previous transactions, and the transaction can be written to a block (6). However, writing to a block is not a straightforward process. The only way to effectively alter a block is to alter that block and all the subsequent blocks, which requires a lot of work (5). This work comes from the process needed to validate a block within the blockchain. “…Bitcoin makes it computationally difficult to hash a block, by requiring that the resulting hash have specific numeric properties.” (7) This is known as proof of work. More specifically, in order to validate the block, a special number called a nonce must be found via random guessing. The correct nonce will create a certain desired hash value, usually ones starting with a certain number of zeros. Finding the correct nonce takes quite a bit of computational work, as well as time. Thus, having to do this multiple times, once for every block affected by changing the blockchain, becomes a nearly infeasible task.

(numbers are my temporary citations lol)
(i also have some images i can add)




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
Hashing Algorithm
Input
Output
Operations
Collision
SHA-0
< 2^64
160 bits
+,and,or,xor,rotl
detected
SHA-1
< 2^64
160 bits
+,and,or,xor,rotl
detected
SHA-224
< 2^64
224 bits
+,and,or,xor,shr,rotr
-
SHA-256
< 2^64
256 bits
+,and,or,xor,shr,rotr
-
SHA-384
< 2^128
384 bits
+,and,or,xor,shr,rotr
-
SHA-512
< 2^128
512 bits
+,and,or,xor,shr,rotr
-

 
SHA-2 Mechanism

*Wikipedia (https://en.wikipedia.org/wiki/SHA-2)

 SHA-256 is a newer, more secure cryptographic hash function which was proposed in 2000 as a new generation of SHA functions and was adopted as FIPS standard in 2002. The SHA-256 algorithm generates a 256-bit hash value from padded 512-bit message blocks, and the original message size is up to 264-1 bits. SHA-256 always computes a 256-bit hash internally for security, but this resulting can be truncated to either 196 or 128 bits printing and storage. Thus a truncated SHA-256 yields a substantial benefit for human usability in printed citations, and significantly improves security, at the cost of a small reduction in performance related to MD5. Unlike the MD5 algorithm, truncated SHA-256 is not subject to any known attacks.

*source: http://www.differencebetween.net/technology/difference-between-sha-256-and-sha-1/#ixzz6wY4odRtm
 
4. Block Analysis
 
Each blocks consist of two parts: Header and Body.

*source:https://www.researchgate.net/figure/The-structure-of-a-Blockchain-A-block-is-composed-of-a-header-and-a-body-where-a-header_fig1_337306138
 

Due to heavy size of the given json, it was impossible/inefficient to load the whole data with limited computing resources. I used ijson python library to read and analyze the json line by line.
(You can also view it from here: https://blockchain.info/block-height/556459?format=json)


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

 

Among header information, what we need to verify the block’s integrity are version, previousblockhash, merkleroot, time, bits, nonce.
After parsing appropriately and applying double SHA-256 hashing algorithm, then we can verify that the block’s header information is correct because any small frauds of the block will result in unpredictable hash values (avalanche effect).



Conclusion


	Source
https://www.youtube.com/watch?v=_160oMzblY8&ab_channel=AndersBrownworthAndersBrownworth
https://en.bitcoin.it/wiki/Transaction
https://en.bitcoin.it/wiki/Protocol_rules#.22tx.22_messages
https://en.bitcoin.it/wiki/Protocol_documentation#BlockTransactions




