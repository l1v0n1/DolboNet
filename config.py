# Токен бота в Discord
# Как получить: https://www.writebots.com/discord-bot-token/
token = "ВСТАВЬТЕ_ТОКЕН_СЮДА"

# С какой вероятностью бот отправит сообщение, если обнаружит сообщение с его упоминанием (от 0 до 1)
mention_prob = 1  # 100%

# С какой вероятностью бот отправит сообщение, если обнаружит сообщение без его упоминания (от 0 до 1)
no_mention_prob = 0.2  # 20%

# Температура семплирования - регулирует характер и разнообразие генерируемого текста
# Примеры значений:
# 0.3  - пресет "попугай-повторюшка"
# 0.65 - пресет "по-умолчанию"
# 1.3  - пресет "пьяный поэт"
# 3    - пресет "уснул на клавиатуре"
temperature = 0.65

# Команда изменения температуры во время работы бота (могут использовать только администраторы)
command_temperature_change = "!temp"

# ---
# ! Следующие параметры лучше оставить как есть !
# ---

# Максимальная длина хранимой очереди сообщений на канал
deque_max_len = 10

# Предобученные веса модели
weights_file = "weights/dolbonet_004_100_0.1485_0.4306.h5"

# Файл хранящий словарь
vocab_file = "vocab/vocab_full_10k_ru.pickle"

# Статус бота в Discord
discord_game_name = "github.com/sergree"

# Величина словаря
vocab_size = 10000

# Максимальная длина входного и выходного тензоров
max_len = 64

# Использовать подготовительный прогон трансформера (читайте why_prewarm.txt)
use_prewarm = True

# Использовать задержку в печати или нет (симуляция скорости печати 300-600 символов в минуту)
use_delay = True
