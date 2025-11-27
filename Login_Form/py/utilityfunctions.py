###############################################################
#
#
#                 utilityfunctions.py
#
#         Author: Brandon Lewis
#           Date: 11/26/2025
#        Updated: 11/26/2025
#
#        Summary: Holds utility functions for the application,
#                 like the ability to set the text of the error field.
#
#
#
################################################################

class ErrorField():
    
    def show_missing_fields(parent):
        missing_fields = []
        for key, value in parent.required_fields.items():
            if key.text() == "" and not key.isReadOnly():
                missing_fields.append(value)
            
            str_to_show = "Missing fields: "
            for i, field in enumerate(missing_fields):
                if i == len(missing_fields) - 1:
                    str_to_show += f"{field}"
                    continue
                str_to_show += f"{field}, "  

        if str_to_show == "Missing fields: ":
            ErrorField.clear_errors(parent)
            return False
        else:
            ErrorField.show_error(parent, str_to_show)
            return True
        
    def show_error(parent, error_message, append=False):
        parent.lblErrors.setVisible(True)
        
        txt_to_show = error_message

        if append:
            previous_text = parent.lblErrors.text()
            txt_to_show += f"\n{previous_text}"

        parent.lblErrors.setText(txt_to_show)

    def clear_errors(parent):
        parent.lblErrors.setVisible(False)
        parent.lblErrors.setText("")


class AllFields():

    def clear_all(parent):
        widgets = [parent.lineUser, parent.lineEmail, parent.linePassConf, parent.linePassCreate]

        for widget in widgets:
            if widget.isReadOnly(): widget.setReadOnly(False)
            widget.clear()