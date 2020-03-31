from enum import Enum


class Message(Enum):
    ENTER = "enter_message"
    ENTER_TERRITORY = "enter_territory_message"
    ENTER_TERRITORY_LEAVE = "enter_territory_leave_message"
    START = "start_message"
    OVERVIEW_INTRO = "overview_intro_message"
    OVERVIEW_CONTENT = "overview_content_message"
    OVERVIEW_END ="overview_end_message"
    OVERVIEW_PEACE ="overview_peace_message"
    OVERVIEW_NO_TERRITORY ="overview_no_territory_message"
    CITIES = "cities"
    COMMAND = "command_message"
    HISTORY = "history_message"
    HISTORY_PEACE = "history_peace_message"
    HISTORY_NO_TERRITORY = "history_no_territory_message"
    LEAVE = "leave_message"
    LEAVE_FORFEIT = "leave_forfeit_message"
    LEAVE_NO_TERRITORY = "leave_no_territory_message"
    COMMAND_SENT = "command_sent_message"
    COMMAND_SENT_PEACE = "command_sent_peace_message"
    COMMAND_NO_TERRITORY = "command_no_territory_message"
    COMMAND_WRONG_CITY_NAME = "command_wrong_city_name_message"
    COMMAND_WRONG_FORMAT="command_wrong_format_message"
    ERROR="error_message"
    UNIT_MOVED="unit_moved_message"
    UNIT_NOT_THERE_MOVE="unit_not_there_move"
    INTERCEPTED="intercepted_message"
    INVADER_ELIMINATED="invader_eliminated_message"
    HELP_NEEDED_AT="help_needed_at_message"
    ENEMY_ELIMINATED="enemy_eliminated"
    LOST_THE_WAR="lost_the_war_message"
    UNDER_SIEGE="under_siege_message"