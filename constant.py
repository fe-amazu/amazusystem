import dotenv, os
dotenv.load_dotenv()

CH_REGISTER = int(os.getenv("CH_REGISTER", "608656664601690142"))
CH_JOIN = int(os.getenv("CH_JOIN", "653923742245978129"))
CH_ROOM_MASTER = int(os.getenv("CH_ROOM_MASTER", "702042912338346114"))
CH_THREAD_MASTER = int(os.getenv("CH_THREAD_MASTER", "702030388033224714"))
CH_VOICE = int(os.getenv("CH_VOICE", "655319117691355166"))
CH_VOICE_TEXT = int(os.getenv("CH_VOICE_TEXT", "655319030428598303"))

CAT_ROOM = int(os.getenv("CAT_ROOM", "702044270609170443"))
CAT_ROOM_ARCHIVE = int(os.getenv("CAT_ROOM_ARCHIVE", "711058666387800135"))
CAT_THREAD = int(os.getenv("CAT_THREAD", "662856289151615025"))
CAT_THREAD_ARCHIVE = int(os.getenv("CAT_THREAD_ARCHIVE", "702074011772911656"))

ROLE_MEMBER = int(os.getenv("ROLE_MEMBER", "652885488197435422"))
ROLE_ARCHIVE = int(os.getenv("ROLE_ARCHIVE", "702420267309203466"))

EMOJI_PIN = str(os.getenv("EMOJI_PIN", "📌"))
