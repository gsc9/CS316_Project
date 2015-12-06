import java.io.IOException;
import java.util.Random;

public class GenRegisteredUser extends AbstractGen {
	
	public GenRegisteredUser(Random randomGenerator, String table, String[] usernames) throws IOException {
		myHardcoded = "CREATE TABLE " + table + " (id INTEGER NOT NULL PRIMARY KEY, username VARCHAR(256) NOT NULL);\n";
		
		StringBuilder sBuilder = new StringBuilder();
		for (int i = 0; i < usernames.length; i++) {
			sBuilder.append("INSERT INTO " + table + " VALUES(" + (i+1) + ", '" + usernames[i] + "');\n");
		}
		
		myData = sBuilder.toString();
	}

	@Override
	protected String[] extractData() {
		return null;
	}
}