package com.galenframework.java.sample.tests;

import java.io.IOException;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.Test;

import com.galenframework.java.sample.components.TecomBase;


public class WelcomePageTest extends TecomBase
{

  @Test(dataProvider = "devices")
    public void welcomePage_onDevice(TestDevice device) throws IOException, InterruptedException
    {
    	load("/");
    		 for (int i=0; i<5; i++)
    		 { 
    			try 
    		    {
   			    Thread.sleep(1000);
  		    }
 			catch (InterruptedException e)
 			{} 			
 		}   			  
 		 checkLayout("/specs/welcomePage.spec", device.getTags());
     }
  
   @Test(dataProvider = "devices")
   public void slider1_onDevice(TestDevice device) throws IOException  {
	
   	load("/");
		 for (int i=0; i<5; i++)
		 { 
		   try 
		   	{
			   Thread.sleep(1000);
			   getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[2]/a[@href='#']")).click();
			
	    }
		catch (InterruptedException e)
	{} 			
	 }
	 
				 
		 checkLayout("/specs/slider1.spec", device.getTags());
   }
   
    @Test(dataProvider = "devices")
    public void slider2_onDevice(TestDevice device) throws IOException  {
   	load("/");
		 for (int i=0; i<5; i++)
		 { 
			try 
		    {
			    Thread.sleep(1000);
			    getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[3]/a[@href='#']")).click();
				
		    }
			catch (InterruptedException e)
			{} 			
		 }

		
		 	 
				 
   checkLayout("/specs/slider2.spec", device.getTags());
 }
    
    @Test(dataProvider = "devices")
    public void slider3_onDevice(TestDevice device) throws IOException  {
    	
   	load("/");
   			 for (int i=0; i<5; i++)
		 { 
			try 
		    {
			    Thread.sleep(1000);
			    getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[4]/a[@href='#']")).click();
			       }
			catch (InterruptedException e)
			{} 			
		 }
	
   				 
   			getDriver().findElement(By.xpath("//div[@class='filter']/div[1]/label[@class='input-container']/span[@class='input-label']")).click();
		    getDriver().findElement(By.xpath("//div[@class='filter']/div[2]/label[@class='input-container']/span[@class='input-label']")).click();
		    getDriver().findElement(By.xpath("//div[@class='filter']/div[3]/label[@class='input-container']/span[@class='input-label']")).click();
	 		
		    JavascriptExecutor jsx = (JavascriptExecutor)getDriver();
		    jsx.executeScript("window.scrollBy(0,300)", "");
		    
     checkLayout("/specs/slider3.spec", device.getTags());
   }
    
    @Test(dataProvider = "devices")
   public void slider4_onDevice(TestDevice device) throws IOException, InterruptedException  {
    	load("/");
   			 for (int i=0; i<5; i++)
    			 { 
  				try 
			    {
    				    Thread.sleep(1000);
    				    getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[5]/a[@href='#']")).click();
    					
			    }
    				catch (InterruptedException e)
    				{} 			
    			 }
   			Actions action = new Actions(getDriver());
   			WebElement we1 = getDriver().findElement(By.xpath("//section[5]//div[@class='section-content']/div/div[2]/div[@class='swiper-wrapper']/div[1]/div"));
   			WebElement we2 = getDriver().findElement(By.xpath("//section[5]//div[@class='section-content']/div/div[2]/div[@class='swiper-wrapper']/div[2]/div"));
   			WebElement we3 = getDriver().findElement(By.xpath("//section[5]//div[@class='section-content']/div/div[2]/div[@class='swiper-wrapper']/div[3]/div"));
   			
   			action.moveToElement(we1).build().perform();
   			Thread.sleep(5000);
   			action.moveToElement(we2).build().perform();
   			Thread.sleep(5000);
   			action.moveToElement(we3).build().perform();
   			
        checkLayout("/specs/slider4.spec", device.getTags());
    }
   
    @Test(dataProvider = "devices")
   public void slider5_onDevice(TestDevice device) throws IOException  {
		
   	load("/");
	 for (int i=0; i<5; i++)
		 { 
 			try 
		    {
		     Thread.sleep(1000);
			 getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[6]/a[@href='#']")).click();
		    }
		catch (InterruptedException e)
		{} 			
		}

       checkLayout("/specs/slider5.spec", device.getTags());
   }
   
  @Test(dataProvider = "devices")
  public void slider6_onDevice(TestDevice device) throws IOException  {
	   load("/");
		 for (int i=0; i<5; i++)
			 { 
				try 
			    {
					Thread.sleep(1000);
					getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[7]/a[@href='#']")).click();
			    }
			catch (InterruptedException e)
			{} 			
			}
 
      checkLayout("/specs/slider6.spec", device.getTags());
  }
    
  @Test(dataProvider = "devices")
   public void slider7_onDevice(TestDevice device) throws IOException  {
	
	   load("/");
		 for (int i=0; i<5; i++)
			 { 
				try 
			    {
			    Thread.sleep(1000);
			    getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[8]/a[@href='#']")).click();
		    }
			catch (InterruptedException e)
			{} 			
			}
		 
		 	 JavascriptExecutor js = (JavascriptExecutor) getDriver();
			 List<WebElement> Element = getDriver().findElements(By.xpath("//section[8]/div[@class='fp-tableCell']/div[@class='fp-scrollable']//a[@href='/']"));
             js.executeScript("arguments[0].scrollIntoView(true);", Element);
		 
			 
       checkLayout("/specs/slider7.spec", device.getTags());
    }
   
	@Test(dataProvider = "devices")
    public void Footer_onDevice(TestDevice device) throws IOException  {
		load("/");
		 for (int i=0; i<5; i++)
		 { 
			try 
		    {
			    Thread.sleep(1000);
			    getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[9]/a[@href='#']/span[2]")).click();
				
		    }
			catch (InterruptedException e)
			{} 			
		 }
		
		 JavascriptExecutor js = (JavascriptExecutor) getDriver();
	//	 List<WebElement> Element = getDriver().findElements(By.xpath("//div[@class='component row-splitter']/div[3]//ul/li[1]/div[@class='field-link']/a[@href='/']"));
		// js.executeScript("arguments[0].scrollIntoView();", Element);
		 js.executeScript("window.scrollBy(0,200)");	 
        checkLayout("/specs/footer.spec", device.getTags());
    }
	
}
   

