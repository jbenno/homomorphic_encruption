# Homomorphic Encryption
## Privacy Preserving Computation

### What is Homomorphic Encryption
Homomorphic encryption (HE) and the “Learning with Errors” methods have been mainly developed since the 2010s.  
The principle is similar to other public/secret key crypto systems: Data is encrypted with a public key and decrypted with a secret key.  
The main feature of HE is that calculations can be executed on the encrypted data without disclosing any of the encrypted information, delivering encrypted results that can be decrypted with the secret key.

#### A very simple example
User Alice generates geo-location data on her smart phone.  
The data is encrypted with HE. The encrypted data is shared with Bob who offers location based services (e.g. recommendations).  
Bob encrypts the location data of his recommendation with Alice’s public key (of course automatically via the app). He can look up in his data base of now encrypted locations which services can be offered to Alice.  

At no point is Alice’s location shared with Bob. (Of course in reality a few more precautions have to be set in place to prevent de-anonymising)

### Code examples
#### Ring-learning-with-errors
Based on Fan, Junfeng, and Frederik Vercauteren. ‘Somewhat Practical Fully Homomorphic Encryption’, 2012. https://eprint.iacr.org/2012/144 .
- Python [RLWE01.py](/code/RLWE01.py)
- Jupyter Notebook [HE01.ipynb](/code/HE01.ipynb)

#### Geo-fencing demo in C#
This demo was done by [Dominik](https://github.com/DominikLindemann), Axel, and myself.  
[Homomorphic Iota](/code/homomorphic_iota)


## Literature
[Literature.md](/files/Literature.md) (will be updated continuously)

