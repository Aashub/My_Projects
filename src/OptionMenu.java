
import java.io.IOException;		
import java.text.DecimalFormat;
import java.util.*;




public class OptionMenu extends Account {
	
	Scanner menuInput = new Scanner(System.in);
	DecimalFormat moneyFormat = new DecimalFormat("'$'###,##0.00");
	
	HashMap<Integer, Integer > data = new HashMap<Integer, Integer>();
	
	
	//Validate login information customer number and pin number
	
	public void getlogin() throws IOException
			{
			 int x = 1;
			 
			 
			 do {
				 try {
					 
					 data.put(913126, 9090);
					 data.put(913127, 9070);
					 
					 System.out.println("Welcome to the ATM Machine");
					 
					 System.out.print("Enter Your Account Number:");
					 setCustomerNumber(menuInput.nextInt());
					 
					 System.out.print("Enter Your Pin Number: ");
					 setPinNumber(menuInput.nextInt());
				 }
				 catch(Exception e)
				 {
					 System.out.println("\n" + "Invalid character(s), Only numbers." + "\n");
					 x = 2;
					 
				 }
				 for(java.util.Map.Entry<Integer, Integer> entry : data.entrySet())
				 {
					 if(entry.getKey() == getCustomerNumber() && entry.getValue() == getPinNumber())
					 {
						 getAccountType();
					 }
					 
				 }
				 System.out.println("\n" + "Wrong Customer Number or Pin Number." + "\n");
				 
			 }while(x == 1);
			}
	
	//Display Account Type Menu with selection
	
	public void getAccountType()
	{
		System.out.println("Select the Account you want to access: ");
		System.out.println("Type 1 - Checking Account");
		System.out.println("Type 2 - Saving Account");
		System.out.println("Type 3 - Exit");
		System.out.print("Choice: ");
		
		selection = menuInput.nextInt();
		
		switch (selection)
		{
		case 1: getChecking();
		break;
		
		case 2: getSaving();
		break;
		
		case 3: 
			System.out.println("Thank you for using this ATM, have a nice day.");	
			getAccountType();
			break;
			
			default:
				System.out.println("\n" + "Invalid Choice." + "\n");
				getAccountType();
		}
	}
	
	//Display Checking Account Menu with selections
	
	public void getChecking()
	{
		System.out.println("Checking Account: ");
		System.out.println("Type 1 - View Balance");
		System.out.println("Type 2 - Withdraw Amount");
		System.out.println("Type 3 - Deposit Amount");
		System.out.println("Type 4 - Exit");
		System.out.print("Choice: ");
		
		selection = menuInput.nextInt();
		
		switch(selection)
		{
		case 1:
			
			System.out.println("Checking Account Balance: " + moneyFormat.format(getCheckingBalance()));
			getAccountType();
			break;
			
		case 2:
			getCheckingWithdrawInput1();
			getAccountType();
			break;
			
		case 3:
			getCheckingDepositInput1();
			getAccountType();
			break;
			
		case 4:
			System.out.println("Thank You for using this ATM, Have a nice Day");
			break;
			
			default:
				System.out.println("\n" + "Invalid choice." + "\n");
		}
	}
	
	//Display SAving Account Menu with selection
	
	public void getSaving()
	{
	System.out.println("Saving Account: ");
	System.out.println("Type 1 - View Balance");
	System.out.println("Type 2 - Withdraw Amount");
	System.out.println("Type 3 - Deposit Amount");
	System.out.println("Type 4 - Exit");
	System.out.println("Choice: ");
	
	selection = menuInput.nextInt();
	
	switch (selection)
	{
	case 1:
		System.out.println("Saving Account Balance: " + moneyFormat.format(getSavingBalance()));
		getAccountType();
		break;
		
	case 2:
		getSavingWithdrawInput11();
		getAccountType();
		break;
		
	case 3:
		getSavingDepositInput();
		getAccountType();
		break;
		
	case 4:
		System.out.println("Thank you for using this ATM, Have a nice DAy");
		break;
		
		default:
			System.out.println("\n" + "Invalid choice." + "\n");
			getSaving();
	}

	
}
	
		
	
	int selection;
}
