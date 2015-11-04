import java.io.IOException;
import java.util.HashSet;
import java.util.Random;

public class GenPartOf extends AbstractGen {
	
	private String[] myPairings;
	
	public GenPartOf(Random randomGenerator, String table, String[] emails, String[] eids) throws IOException {
		String hardcoded = "CREATE TABLE " + table + " (email VARCHAR(256) NOT NULL REFERENCES Registered_User(email), eid INTEGER NOT NULL REFERENCES Event(eid), is_admin BOOLEAN NOT NULL, PRIMARY KEY(email, eid));";
		HashSet<Integer> pastEids = new HashSet<Integer>();
		
		// CHANGE TABLE SIZE HERE!!!
		int PRODUCTION_SIZE = 20000;
		// CHANGE TABLE SIZE HERE!!!
		
		myPairings = new String[PRODUCTION_SIZE];
		
		StringBuilder sBuilder = new StringBuilder(hardcoded + "\n");
		for (int i = 0; i < PRODUCTION_SIZE; i++) {
			String admin = "FALSE";
			int chosenUser = randomGenerator.nextInt(emails.length / 2);
			int chosenEvent = randomGenerator.nextInt(eids.length / 2);
			myPairings[i] = emails[chosenUser] + "', " + eids[chosenEvent];
			if (!pastEids.contains(chosenEvent)) {
				pastEids.add(chosenEvent);
				admin = "TRUE";
			}
			else {
				if (randomGenerator.nextInt(10) == 5) {
					admin = "TRUE";
				}
			}
			sBuilder.append("INSERT INTO " + table + " VALUES('" + myPairings[i] + ", " + admin + ");\n");
		}
		
		myData = sBuilder.toString();
	}
	
	@Override
	protected String[] extractData() {
		return myPairings;
	}
}