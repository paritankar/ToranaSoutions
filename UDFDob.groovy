import java.text.SimpleDateFormat;
import java.util.Date;
import java.text.ParseException;
import java.time.format.DateTimeFormatter;  
import java.time.LocalDateTime;   
 
 
 class UDFDob {
        
       

        public static boolean isDateValid(String strDate) 
        {
            SimpleDateFormat sdfrmt = new SimpleDateFormat("dd-MM-yyyy");
	        sdfrmt.setLenient(false);
			DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");  
            LocalDateTime now = LocalDateTime.now(); 
			
            try
	            {
	                Date javaDate = sdfrmt.parse(strDate); 
	                System.out.println(strDate+" is valid date format");
	            }

            catch (ParseException e)
	            {
	                System.out.println(strDate+" is Invalid Date format");
	                return false;
	            }
			Date javaDate = sdfrmt.parse(strDate); 
			Date CurrentDate = sdfrmt.parse(dtf.format(now)); 
			if (javaDate.before(CurrentDate))
				{
				return true;
				}
			else
			{
				return false;
			}
}
}