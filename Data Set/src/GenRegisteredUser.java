import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Random;

public class GenRegisteredUser extends AbstractGen {
	
	private String[] myEmails;
	
	public GenRegisteredUser(Random randomGenerator, String table) throws IOException {
		String hardcoded = "CREATE TABLE " + table + " (email VARCHAR(256) NOT NULL PRIMARY KEY, username VARCHAR(256) NOT NULL);";
		String[] firstNames = firstNames();
		String[] lastNames = lastNames();
		HashSet<String> names = new HashSet<String>();
		
		// CHANGE TABLE SIZE HERE!!!
		int PRODUCTION_SIZE = 10000;
		// CHANGE TABLE SIZE HERE!!!
		
		StringBuilder eBuilder = new StringBuilder();
		StringBuilder sBuilder = new StringBuilder(hardcoded + "\n");
		for (int i = 0; i < PRODUCTION_SIZE; i++) {
			int firstIndex = randomGenerator.nextInt(firstNames.length - 1);
			int lastIndex = randomGenerator.nextInt(lastNames.length - 1);
			String newName = firstNames[firstIndex] + " " + lastNames[lastIndex];
			if (!names.contains(newName)) {
				names.add(newName);
				String email = firstNames[firstIndex] + "." + lastNames[lastIndex] + "@example.com";
				sBuilder.append("INSERT INTO " + table + " VALUES('" + email + "', '" + newName + "');\n");
				eBuilder.append(email + "\n");
			}
		}
		
		myEmails = eBuilder.toString().split("\n");
		myData = sBuilder.toString();
	}
	
	@Override
	protected String[] extractData() {
		return myEmails;
	}
	
	private String[] lastNames() throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(this.getClass().getResourceAsStream("/resources/Last Names.txt")));
		StringBuilder sBuilder = new StringBuilder();
		String line = in.readLine();
		while (line != null) {
			sBuilder.append(line.split(" ")[0].toLowerCase() + "\n");
			line = in.readLine();
		}
		in.close();
		return sBuilder.toString().split("\n");
	}
	
	private String[] firstNames() throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(this.getClass().getResourceAsStream("/resources/Female Names.txt")));
		StringBuilder sBuilder = new StringBuilder();
		String line = in.readLine();
		while (line != null) {
			sBuilder.append(line.split(" ")[0].toLowerCase() + "\n");
			line = in.readLine();
		}
		in.close();
		
		in = new BufferedReader(new InputStreamReader(this.getClass().getResourceAsStream("/resources/Male Names.txt")));
		line = in.readLine();
		while (line != null) {
			sBuilder.append(line.split(" ")[0].toLowerCase() + "\n");
			line = in.readLine();
		}
		in.close();
		return sBuilder.toString().split("\n");
	}
}