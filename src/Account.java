
import java.text.DecimalFormat;
import java.util.Scanner;

public class Account {
	
Scanner input = new Scanner(System.in);
DecimalFormat moneyFormat = new DecimalFormat("'$'###,##0.00");


//set the customer number

public int setCustomerNumber(int customerNumber)
{
	this.customerNumber = customerNumber;
	return customerNumber;
}

//Get the customer number

public int getCustomerNumber()
{
	return customerNumber;
}

//Set pin Number

public int setPinNumber(int pinNumber)
{
	this.pinNumber = pinNumber;
	return pinNumber;
	
}

//Get pin number
public int getPinNumber()
{
	return pinNumber;
}

//get checking account balance

public double getCheckingBalance()
{
	return checkingBalance;
}

//get saving Account Balance

public double getSavingBalance()
{
	return savingBalance;
}


//calculate checking Account withdraw

public double calcCheckingWithdraw(double amount)
{
	checkingBalance = (checkingBalance - amount);
	return checkingBalance;
}

//calculate saving Account withdraw

public double calcSavingWithdraw(double amount)
{
	savingBalance = (savingBalance - amount);
	return savingBalance;
}

//calculate checking account deposit

public double calcCheckingdeposit(double amount)
{
	checkingBalance = (checkingBalance + amount);
			return checkingBalance;
}

//calculate saving account deposit

public double calcSavingdeposit(double amount)
{
	savingBalance = (savingBalance + amount);
			return savingBalance;
}


//customer checking account withdraw input

public void getCheckingWithdrawInput1()
{
	System.out.println("Checking Account Balance: " + moneyFormat.format(checkingBalance));
	System.out.println("Amount you want to withdraw from Checking Account: ");
	double amount = input.nextDouble();
	
	if((checkingBalance - amount) >= 0)
	{
		calcCheckingWithdraw(amount);
		System.out.println("New Checking Account balance: " + moneyFormat.format(checkingBalance));
		
	}
	else
	{
		System.out.println("Balance cannot be negative." + "\n");
	}
}

//customer SAving account withdraw input

public void getSavingWithdrawInput11()
{
	System.out.println("Saving Account Balance:" + moneyFormat.format(savingBalance));
	System.out.print("Amount you want to withdraw from Saving Account:  ");
	double amount = input.nextDouble();
	

if((savingBalance - amount) >= 0)
{
	calcSavingWithdraw(amount);
	System.out.println("New Saving Account Balance: " + moneyFormat.format(savingBalance));
	
}
else
{
	System.out.println("Balance cannot be negative." + "\n");
}


}

//customer checking account deposit input
public void getCheckingDepositInput1()
{
	System.out.println("Checking Account Balance:" + moneyFormat.format(checkingBalance));
	System.out.print("Amount you want to Deposit in Checking Account:  ");
	double amount = input.nextDouble();
	

if((checkingBalance + amount) >= 0)
{
	calcCheckingdeposit(amount);
	System.out.println("New Checking Account Balance: " + checkingBalance + "\n");
	
}
else
{
	System.out.println("Balance cannot be negative." + "\n");
}

}

//customer saving account deposit input

public void getSavingDepositInput()
{
	System.out.println("Saving Account Balance: " + moneyFormat.format(savingBalance));
	System.out.println("Amount you want to Deposit in Saving Account: ");
	double amount = input.nextDouble();
	
	if((savingBalance + amount) >= 0)
	{
		calcSavingdeposit(amount);
		System.out.println("New Saving Account Balance: " + savingBalance + "\n");
		
	}
	else
	{
		System.out.println("Balance cannot be negative." + "\n");
	}
}
private int customerNumber;
private int pinNumber;
private double checkingBalance = 0;
private double savingBalance = 0;
}
