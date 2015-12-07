import java.io.IOException;
import java.util.HashSet;
import java.util.Random;

public class GenPartOf extends AbstractGen {
	
	private String[] myPairings;
	
	public GenPartOf(Random randomGenerator, String table, String[] usernames, String[] eids) throws IOException {
		myHardcoded = "CREATE TABLE " + table + " (uid INTEGER NOT NULL UNIQUE PRIMARY KEY, id INTEGER NOT NULL REFERENCES Registered_User(id), eid INTEGER NOT NULL REFERENCES Event(eid), is_admin BOOLEAN NOT NULL, UNIQUE(id, eid));\n";
		HashSet<Integer> pastEids = new HashSet<Integer>();
		
		// CHANGE TABLE SIZE HERE!!!
		int PRODUCTION_SIZE = 20000;
		// CHANGE TABLE SIZE HERE!!!
		
		myPairings = new String[PRODUCTION_SIZE];
		
		StringBuilder sBuilder = new StringBuilder();
		for (int i = 0; i < PRODUCTION_SIZE; i++) {
			String admin = "FALSE";
			int chosenUser = randomGenerator.nextInt(usernames.length / 2);
			int chosenEvent = randomGenerator.nextInt(eids.length / 2);
			myPairings[i] = chosenUser + ", " + eids[chosenEvent];
			if (!pastEids.contains(chosenEvent)) {
				pastEids.add(chosenEvent);
				admin = "TRUE";
			}
			else {
				if (randomGenerator.nextInt(10) == 5) {
					admin = "TRUE";
				}
			}
			sBuilder.append("INSERT INTO " + table + " VALUES(" + (i+1) + ", " + myPairings[i] + ", " + admin + ");\n");
		}
		
		myData = sBuilder.toString();
	}
	
	@Override
	protected String[] extractData() {
		return myPairings;
	}
}