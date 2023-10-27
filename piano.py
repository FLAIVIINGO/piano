from piano_display import PianoDisplay

piano_ui: PianoDisplay
img_path: str

piano_ui = PianoDisplay()

try:
  piano_ui.window.mainloop()
except Exception as e:
  print(e)