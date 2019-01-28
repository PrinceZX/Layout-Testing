package com.galenframework.java.sample.components;

import static java.util.Arrays.asList;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.concurrent.TimeUnit;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.DataProvider;

import com.galenframework.testng.GalenTestNgTestBase;

public abstract class TecomBase extends GalenTestNgTestBase {

    private static final String ENV_URL = "http://tecomdigitaldev01.northeurope.cloudapp.azure.com/";

    @Override
    public WebDriver createDriver(Object[] args) 
    {
    	System.setProperty("webdriver.chrome.driver", "C:\\Karan\\JAVA JAR\\chromedriver.exe");
    //	System.setProperty("webdriver.firefox.driver1", "C:\\Karan\\JAVA JAR\\geckodriver.exe");
    	 
    	WebDriver driver = new ChromeDriver();
    	//WebDriver driver1 = new FirefoxDriver();
    	
    	 
        if (args.length > 0) {
            if (args[0] != null && args[0] instanceof TestDevice) {
                TestDevice device = (TestDevice)args[0];
                if (device.getScreenSize() != null) {
                    driver.manage().window().setSize(device.getScreenSize());
                    
                    driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
             
                    File scrFile = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
                    try {
						FileUtils.copyFile(scrFile, new File("C:\\Karan\\Projects\\A Working Projects\\TecomProjectTest\\ScreenShot\\failed-test.png"));
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
                    
                             
                }
            }
        }
        
        
        return driver;
    }

    public void load(String uri) {
        getDriver().get(ENV_URL + uri);
    }

    @DataProvider(name = "devices")
    public Object [][] devices () {
        return new Object[][] {
        		{new TestDevice("desktop", new Dimension(1280, 720), asList("desktop"))},
        		{new TestDevice("mobile", new Dimension(450, 800), asList("mobile"))},
                {new TestDevice("tablet", new Dimension(750, 800), asList("tablet"))}
        		
        	
        	
        };
    }

    public static class TestDevice {
        private final String name;
        private final Dimension screenSize;
        private final List<String> tags;

        public TestDevice(String name, Dimension screenSize, List<String> tags) {
            this.name = name;
            this.screenSize = screenSize;
            this.tags = tags;
        }

        public String getName() {
            return name;
        }

        public Dimension getScreenSize() {
            return screenSize;
        }

        public List<String> getTags() {
            return tags;
        }
        
      
        
        @Override
        public String toString() {
            return String.format("%s %dx%d", name, screenSize.width, screenSize.height);
        }
        
        
    }
}
