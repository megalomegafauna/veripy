from behave import then

from veripy.utils.browsers import screenshot_bytes


@then('take a screen shot')
def take_screen_shot(context):
    """ Have the browser take a screenshot of the current window. """
    context.step.screenshots.append(screenshot_bytes(context))
