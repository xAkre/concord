import enum

from concord.gateway.resources import User

__all__ = (
    "LanguageCode",
    "LanguageDisplayName",
    "OAuth2Scopes",
)


class LanguageCode(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/reference#locales) for Discord's
    documentation.
    """

    BULGARIAN = "bg"
    CHINESE_CHINA = "zh-CN"
    CHINESE_TAIWAN = "zh-TW"
    CROATIAN = "hr"
    CZECH = "cs"
    DANISH = "da"
    DUTCH = "nl"
    ENGLISH_UK = "en-GB"
    ENGLISH_US = "en-US"
    FINNISH = "fi"
    FRENCH = "fr"
    GERMAN = "de"
    GREEK = "el"
    HINDI = "hi"
    HUNGARIAN = "hu"
    INDONESIAN = "id"
    ITALIAN = "it"
    JAPANESE = "ja"
    KOREAN = "ko"
    LITHUANIAN = "lt"
    NORWEGIAN = "no"
    POLISH = "pl"
    PORTUGUESE_BRAZILIAN = "pt-BR"
    ROMANIAN = "ro"
    RUSSIAN = "ru"
    SPANISH = "es-ES"
    SPANISH_LATAM = "es-419"
    SWEDISH = "sv-SE"
    THAI = "th"
    TURKISH = "tr"
    UKRAINIAN = "uk"
    VIETNAMESE = "vi"


class LanguageDisplayName(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/reference#locales) for Discord's
    documentation.
    """

    BULGARIAN = "български"
    CHINESE_CHINA = "中文"
    CHINESE_TAIWAN = "繁體中文"
    CROATIAN = "Hrvatski"
    CZECH = "Čeština"
    DANISH = "Dansk"
    DUTCH = "Nederlands"
    ENGLISH_UK = "English, UK"
    ENGLISH_US = "English, US"
    FINNISH = "Suomi"
    FRENCH = "Français"
    GERMAN = "Deutsch"
    GREEK = "Ελληνικά"
    HINDI = "हिन्दी"
    HUNGARIAN = "Magyar"
    INDONESIAN = "Bahasa Indonesia"
    ITALIAN = "Italiano"
    JAPANESE = "日本語"
    KOREAN = "한국어"
    LITHUANIAN = "Lietuviškai"
    NORWEGIAN = "Norsk"
    POLISH = "Polski"
    PORTUGUESE_BRAZILIAN = "Português do Brasil"
    ROMANIAN = "Română"
    RUSSIAN = "Pусский"
    SPANISH = "Español"
    SPANISH_LATAM = "Español, LATAM"
    SWEDISH = "Svenska"
    THAI = "ไทย"
    TURKISH = "Türkçe"
    UKRAINIAN = "Українська"
    VIETNAMESE = "Tiếng Việt"


class OAuth2Scopes(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/topics/oauth2#shared-resources-oauth2-scopes) for Discord's
    documentation.
    """

    ACTIVITIES_READ = "activities.read"
    ACTIVITIES_WRITE = "activities.write"
    APPLICATIONS_BUILDS_READ = "applications.builds.read"
    APPLICATIONS_BUILDS_UPLOAD = "applications.builds.upload"
    APPLICATIONS_COMMANDS = "applications.commands"
    APPLICATIONS_COMMANDS_UPDATE = "applications.commands.update"
    APPLICATIONS_COMMANDS_PERMISSIONS_UPDATE = (
        "applications.commands.permissions.update"
    )
    APPLICATIONS_ENTITLEMENTS = "applications.entitlements"
    APPLICATIONS_STORE_UPDATE = "applications.store.update"
    BOT = "bot"
    CONNECTIONS = "connections"
    DM_CHANNELS_READ = "dm_channels.read"
    EMAIL = "email"
    GDM_JOIN = "gdm.join"
    GUILDS = "guilds"
    GUILDS_JOIN = "guilds.join"
    GUILDS_MEMBERS_READ = "guilds.members.read"
    IDENTIFY = "identify"
    MESSAGES_READ = "messages.read"
    RELATIONSHIPS_READ = "relationships.read"
    ROLE_CONNECTIONS_WRITE = "role_connections.write"
    RPC = "rpc"
    RPC_ACTIVITIES_WRITE = "rpc.activities.write"
    RPC_NOTIFICATIONS_READ = "rpc.notifications.read"
    RPC_VOICE_READ = "rpc.voice.read"
    RPC_VOICE_WRITE = "rpc.voice.write"
    VOICE = "voice"
    WEBHOOK_INCOMING = "webhook.incoming"


class Permissions(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/topics/permissions) for Discord's
    documentation.
    """

    CREATE_INSTANT_INVITE = 1 << 0
    KICK_MEMBERS = 1 << 1
    BAN_MEMBERS = 1 << 2
    ADMINISTRATOR = 1 << 3
    MANAGE_CHANNELS = 1 << 4
    MANAGE_GUILD = 1 << 5
    ADD_REACTIONS = 1 << 6
    VIEW_AUDIT_LOG = 1 << 7
    PRIORITY_SPEAKER = 1 << 8
    STREAM = 1 << 9
    VIEW_CHANNEL = 1 << 10
    SEND_MESSAGES = 1 << 11
    SEND_TTS_MESSAGES = 1 << 12
    MANAGE_MESSAGES = 1 << 13
    EMBED_LINKS = 1 << 14
    ATTACH_FILES = 1 << 15
    READ_MESSAGE_HISTORY = 1 << 16
    MENTION_EVERYONE = 1 << 17
    USE_EXTERNAL_EMOJIS = 1 << 18
    VIEW_GUILD_INSIGHTS = 1 << 19
    CONNECT = 1 << 20
    SPEAK = 1 << 21
    MUTE_MEMBERS = 1 << 22
    DEAFEN_MEMBERS = 1 << 23
    MOVE_MEMBERS = 1 << 24
    USE_VAD = 1 << 25
    CHANGE_NICKNAME = 1 << 26
    MANAGE_NICKNAMES = 1 << 27
    MANAGE_ROLES = 1 << 28
    MANAGE_WEBHOOKS = 1 << 29
    MANAGE_GUILD_EXPRESSIONS = 1 << 30
    USE_APPLICATION_COMMANDS = 1 << 31
    REQUEST_TO_SPEAK = 1 << 32
    MANAGE_EVENTS = 1 << 33
    MANAGE_THREADS = 1 << 34
    CREATE_PUBLIC_THREADS = 1 << 35
    CREATE_PRIVATE_THREADS = 1 << 36
    USE_EXTERNAL_STICKERS = 1 << 37
    SEND_MESSAGES_IN_THREADS = 1 << 38
    USE_EMBEDDED_ACTIVITIES = 1 << 39
    MODERATE_MEMBERS = 1 << 40
    VIEW_CREATOR_MONETIZATION_ANALYTICS = 1 << 41
    USE_SOUNDBOARD = 1 << 42
    CREATE_GUILD_EXPRESSION = 1 << 43
    CREATE_EVENTS = 1 << 44
    USE_EXTERNAL_SOUNDS = 1 << 45
    SEND_VOICE_MESSAGES = 1 << 46
    SEND_POLLS = 1 << 49
    USE_EXTERNAL_APPS = 1 << 50
