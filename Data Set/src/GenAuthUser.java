import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Random;

public class GenAuthUser extends AbstractGen {
	
	private String[] myUsernames;
	private String[] myEmails;
	
	public GenAuthUser(Random randomGenerator, String table) throws IOException {
		String[] firstNames = firstNames();
		String[] lastNames = lastNames();
		String[] passwords = passwords();
		HashSet<String> names = new HashSet<String>();
		
		// CHANGE TABLE SIZE HERE!!!
		int PRODUCTION_SIZE = 10000;
		// CHANGE TABLE SIZE HERE!!!
		
		StringBuilder uBuilder = new StringBuilder();
		StringBuilder eBuilder = new StringBuilder();
		StringBuilder sBuilder = new StringBuilder();
		for (int i = 0; i < PRODUCTION_SIZE; i++) {
			int firstIndex = randomGenerator.nextInt(firstNames.length - 1);
			int lastIndex = randomGenerator.nextInt(lastNames.length - 1);
			int passIndex = randomGenerator.nextInt(passwords.length - 1);
			String firstName = firstNames[firstIndex];
			String lastName = lastNames[lastIndex];
			String newName = firstName + " " + lastName;
			String password = passwords[passIndex];
			if (!names.contains(newName)) {
				names.add(newName);
				String email = firstName + "." + lastName + "@example.com";
				sBuilder.append("INSERT INTO " + table + " VALUES(DEFAULT, '" + password + "', null, false, '" + newName + "', '" + firstName + "', '" + lastName + "', '" + email + "', false, true, '1994-01-22');\n");
				uBuilder.append(newName + "\n");
				eBuilder.append(email + "\n");
			}
		}
		
		myUsernames = uBuilder.toString().split("\n");
		myEmails = eBuilder.toString().split("\n");
		myData = sBuilder.toString();
	}
	
	@Override
	protected String[] extractData() {
		return myUsernames;
	}
	
	@Override
	protected String[] extractMoreData() {
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
	
	private String[] passwords() throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(this.getClass().getResourceAsStream("/resources/Common Passwords.txt")));
		StringBuilder sBuilder = new StringBuilder();
		String line = in.readLine();
		while (line != null) {
			sBuilder.append(line.split(" ")[0] + "\n");
			line = in.readLine();
		}
		in.close();
		return sBuilder.toString().split("\n");
	}
}