<h3>Password_Vault for fetching server password using Python</h3><br>


<b>Basic Flow of the Application :</b>
 1. User will open the Application console and enter:<br>
&nbsp;&nbsp;&nbsp;&nbsp; i.&nbsp;Login credentials<br>
&nbsp;&nbsp;&nbsp;&nbsp; ii.&nbsp;Server detail : ServerName, UserID on server, and Reason for password requirement.<br>
2. Details will be passed to server using API Call<br>
3. Server will first authenticate user<br>
4. Once authenticated will fetch the password from Database which will already be encrypted using the key which is stored on user end.<br>
5. The returned password will first be decrypted using the key stored at User end and then will be displayed on the application interface to be used further.<br>



 
<b> Libraries used :</b>
 1. PyQt5(For Application Interface)<br>
 2. Flask (For Building API) : can refer to my repository Api_Building : <a href="https://github.com/Manish-Lalwani/Api_Building">Repository_Link</a>
 3. MySql ( For Database and it's connectivity) : can refer to my repository Database : <a href="https://github.com/Manish-Lalwani/Database">Repository_Link</a>
 4. Cryptography(For encryption): can refer to my repository Cryptography : <a href="https://github.com/Manish-Lalwani/Crytography">Repository_Link</a>
 
 
 
