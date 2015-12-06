import java.io.IOException;
import java.util.Random;

public class GenRegisteredUser extends AbstractGen {
	
	public GenRegisteredUser(Random randomGenerator, String table, String[] usernames, String[] emails) throws IOException {
		String hardcoded = "CREATE TABLE " + table + " (email VARCHAR(256) NOT NULL PRIMARY KEY, username VARCHAR(256) NOT NULL);";
		
		StringBuilder sBuilder = new StringBuilder(hardcoded + "\n");
		for (int i = 0; i < usernames.length; i++) {
			sBuilder.append("INSERT INTO " + table + " VALUES('" + emails[i] + "', '" + usernames[i] + "');\n");
		}
		
		myData = sBuilder.toString();
	}

	@Override
	protected String[] extractData() {
		return null;
	}
}