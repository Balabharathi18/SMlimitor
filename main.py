from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock
from plyer import notification
import time

class SocialMediaLimitApp(App):
    def build(self):
        self.app_limit = 0  # Time limit in seconds
        self.current_time = 0  # Current time spent on app

        # Main layout of the app
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Time limit input field
        self.time_limit_input = TextInput(hint_text='Enter time limit in minutes', input_filter='int', multiline=False)
        self.layout.add_widget(self.time_limit_input)

        # Set time limit button
        self.start_button = Button(text="Set Time Limit", on_press=self.set_time_limit)
        self.layout.add_widget(self.start_button)

        # Timer label (shows how much time has passed)
        self.timer_label = Label(text="Time Spent: 0 minutes")
        self.layout.add_widget(self.timer_label)

        # Lock social media button
        self.lock_button = Button(text="Lock Social Media", on_press=self.lock_social_media)
        self.layout.add_widget(self.lock_button)

        return self.layout

    def set_time_limit(self, instance):
        """Set the time limit for the social media app."""
        try:
            self.app_limit = int(self.time_limit_input.text) * 60  # Convert minutes to seconds
            self.current_time = 0
            self.start_timer()
        except ValueError:
            self.show_error_popup("Invalid input. Please enter a valid number.")

    def start_timer(self):
        """Start the timer and update it every second."""
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        """Update the current time spent on social media."""
        if self.current_time >= self.app_limit:
            self.stop_timer()
            self.lock_social_media()
            return
        
        self.current_time += 1
        minutes = self.current_time // 60
        self.timer_label.text = f"Time Spent: {minutes} minutes"
    
    def stop_timer(self):
        """Stop the timer once the limit is reached."""
        Clock.unschedule(self.timer_event)

    def lock_social_media(self):
        """Lock the social media app (this would be platform-specific)."""
        if self.current_time >= self.app_limit:
            notification.notify(
                title='Time Up!',
                message="You have exceeded your social media usage time limit.",
                timeout=5
            )
            # Here you can add functionality to lock the app on Android (using Android APIs)
            self.show_error_popup("Time's up! Social media is locked.")

    def show_error_popup(self, message):
        """Show an error message in a popup."""
        popup = Popup(title="Error", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()


if __name__ == '__main__':
    SocialMediaLimitApp().run()
