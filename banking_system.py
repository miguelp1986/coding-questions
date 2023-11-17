"""
In this challenge, simulate a banking system. Create the Account and Transaction classes.
1. The Account class has a data member int balance, initially assigned to zero. The class should implement the following three methods:
1. String deposit(int money) to add money to the balance. This method should return a string that describes the deposit transaction, i.e.,
"Depositing Smoney"
2. String withdraw(int money) to subtract money from the balance. This method should return a string that describes the withdraw transaction, i.e., "Withdrawing Smoney". Note that, if there is insufficient balance to successfully withdraw the desired amount, then the balance should not be adjusted, and the returned string should be "Withdrawing Smoney (Insufficient Balance)".
3. int getBalance() to return the account balance.
2. The Transaction class has two data members
Account account and List<String> transactions. The class should implement the following three methods:
1. void deposit(int money) to invoke the deposit method in the Account class. This should add the transaction message to the transactions list.
2. void withdraw(int money) to invoke the withdraw method in the Account class. This should add the transaction message to the transactions list.
3. List<String> getTransaction) to return the transactions.
Evaluation
The locked stub code in the editor validates the correctness of the Account and Transaction class implementations by making deposit and withdrawal transactions using threads.
"""
