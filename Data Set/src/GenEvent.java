import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;

public class GenEvent extends AbstractGen {
	
	private String[] myEids;
	
	public GenEvent(Random randomGenerator, String table, String[] descriptions) throws IOException {
		String hardcoded = "CREATE TABLE " + table + " (eid INTEGER NOT NULL UNIQUE PRIMARY KEY, title VARCHAR(256) NOT NULL, date DATE NOT NULL, time TIME NOT NULL, location VARCHAR(256) NOT NULL, description VARCHAR(400));";
		String[] titles = titles(descriptions);
		String[] locations = locations();
		
		// CHANGE TABLE SIZE HERE!!!
		int PRODUCTION_SIZE = 10000;
		// CHANGE TABLE SIZE HERE!!!
		
		myEids = new String[PRODUCTION_SIZE];
		String[] dates = dates(PRODUCTION_SIZE, randomGenerator);
		String[] times = times(PRODUCTION_SIZE, randomGenerator);
		
		StringBuilder sBuilder = new StringBuilder(hardcoded + "\n");
		for (int i = 1; i < PRODUCTION_SIZE + 1; i++) {
			myEids[i-1] = "" + i;
			int descIndex = randomGenerator.nextInt(descriptions.length * 5);
			String description = "NULL";
			if (descIndex < descriptions.length - 1) {
				description = "'" + descriptions[descIndex] + "'";
			}
			int titleIndex = randomGenerator.nextInt(titles.length - 1);
			int locationIndex = randomGenerator.nextInt(locations.length - 1);
			sBuilder.append("INSERT INTO " + table + " VALUES(" + i + ", '" + titles[titleIndex] + "', '" + dates[i-1] + "', '" + times[i-1] + "', '" + locations[locationIndex] + "', " + description + ");\n");
		}
		
		myData = sBuilder.toString();
	}
	
	@Override
	protected String[] extractData() {
		return myEids;
	}
	
	private String[] titles(String[] descriptions) {
		String[] titles = new String[descriptions.length - 1];
		for (int i = 0; i < descriptions.length - 1; i++) {
			String[] strArray = descriptions[i].split(" ");
			titles[i] = strArray[0] + " " + strArray[1] + " " + "event";
		}
		return titles;
	}
	
	private String[] locations() throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(this.getClass().getResourceAsStream("/resources/Cities.txt")));
		StringBuilder sBuilder = new StringBuilder();
		String line = in.readLine();
		while (line != null) {
			sBuilder.append(line + "\n");
			line = in.readLine();
		}
		in.close();
		return sBuilder.toString().split("\n");
	}
	
	private String[] dates(int size, Random rGen) {
		String[] dateArray = new String[size];
		for (int i = 0; i < size; i++) {
			int year = rGen.nextInt(11) + 2010;
			int month = rGen.nextInt(12) + 1;
			int day = rGen.nextInt(28) + 1;			
			String balancer1 = "";
			if (month < 10) {
				balancer1 = "0";
			}
			String balancer2 = "";
			if (day < 10) {
				balancer2 = "0";
			}
			dateArray[i] = year + "-" + balancer1 + month + "-" + balancer2 + day;
		}
		return dateArray;
	}
	
	private String[] times(int size, Random rGen) {
		String[] timeArray = new String[size];
		for (int i = 0; i < size; i++) {
			int hour = rGen.nextInt(14) + 8;
			int minute = rGen.nextInt(4) * 15;
			String balancer1 = "";
			if (hour < 10) {
				balancer1 = "0";
			}
			String balancer2 = "";
			if (minute == 0) {
				balancer2 = "0";
			}
			timeArray[i] = balancer1 + hour + ":" + balancer2 + minute + ":00";
		}
		return timeArray;
	}
}