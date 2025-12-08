from tkinter import ttk, filedialog, messagebox, Text
import io
import contextlib
from introduction import print_help
from controllers.password_controller import PasswordController
from controllers.file_controller import FileController

# inspired by AI

class UI:
    def __init__(self, root):
        self.root = root
        self.encryptor = None
        self.decryptor = None
        self.password_controller = PasswordController()
        self.file_controller = FileController()
        self._current_frame = None
        self._pw1_var = None
        self._pw2_var = None

    def start(self):
        self._show_password_view()

    def _clear_frame(self):
        if self._current_frame is not None:
            self._current_frame.destroy()
        self._current_frame = ttk.Frame(master=self.root, padding=20)
        self._current_frame.pack(fill="both", expand=True)

    def _show_password_view(self):
        self._clear_frame()
        ttk.Label(self._current_frame, text="CipherVault - set password").grid(
            row=0, column=0, columnspan=2, pady=(0, 10)
        )
        ttk.Label(self._current_frame, text="Password:").grid(row=1, column=0, sticky="e")
        ttk.Label(self._current_frame, text="Repeat password:").grid(row=2, column=0, sticky="e")
        self._pw1_var = ttk.Entry(self._current_frame, show="*")
        self._pw2_var = ttk.Entry(self._current_frame, show="*")
        self._pw1_var.grid(row=1, column=1, pady=2, sticky="we")
        self._pw2_var.grid(row=2, column=1, pady=2, sticky="we")
        self._current_frame.columnconfigure(1, weight=1)
        continue_button = ttk.Button(
            self._current_frame,
            text="Continue",
            command=self._handle_password_ok,
            takefocus=True,
        )
        continue_button.grid(row=3, column=0, columnspan=2, pady=10)
        continue_button.bind("<Return>", lambda event: self._handle_password_ok())
        self._pw1_var.focus_set()

    def _handle_password_ok(self):
        pw1 = self._pw1_var.get()
        pw2 = self._pw2_var.get()
        encryptor, decryptor, error = self.password_controller.validate_and_create_engines(pw1, pw2)
        if error:
            messagebox.showerror("Error", error)
            return
        self.encryptor = encryptor
        self.decryptor = decryptor
        self._show_main_view()

    def _show_main_view(self):
        self._clear_frame()
        ttk.Label(self._current_frame, text="CipherVault").pack(pady=10)
        encrypt_button = ttk.Button(
            self._current_frame,
            text="Encrypt file",
            command=self.encrypt_file,
            takefocus=True,
        )
        encrypt_button.pack(pady=5)
        encrypt_button.bind("<Return>", lambda e: self.encrypt_file())
        decrypt_button = ttk.Button(
            self._current_frame,
            text="Decrypt file",
            command=self.decrypt_file,
            takefocus=True,
        )
        decrypt_button.pack(pady=5)
        decrypt_button.bind("<Return>", lambda e: self.decrypt_file())
        help_button = ttk.Button(
            self._current_frame,
            text="Help",
            command=self.show_help,
            takefocus=True,
        )
        help_button.pack(pady=5)
        help_button.bind("<Return>", lambda e: self.show_help())
        quit_button = ttk.Button(
            self._current_frame,
            text="Quit",
            command=self.root.quit,
            takefocus=True,
        )
        quit_button.pack(pady=5)
        quit_button.bind("<Return>", lambda e: self.root.quit())
        encrypt_button.focus_set()

    def encrypt_file(self):
        inp = filedialog.askopenfilename(title="Select file to encrypt")
        if not inp:
            return
        out = filedialog.asksaveasfilename(title="Enter output file")
        if not out:
            return
        success, msg = self.file_controller.encrypt(self.encryptor, inp, out)
        if success:
            messagebox.showinfo("Result", msg)
        else:
            messagebox.showerror("Error", msg)

    def decrypt_file(self):
        inp = filedialog.askopenfilename(title="Select file to decrypt")
        if not inp:
            return
        out = filedialog.asksaveasfilename(title="Enter output file")
        if not out:
            return
        success, msg = self.file_controller.decrypt(self.decryptor, inp, out)
        if success:
            messagebox.showinfo("Result", msg)
        else:
            messagebox.showerror("Error", msg)

    def show_help(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            print_help()
        help_text = buf.getvalue()
        self._clear_frame()
        ttk.Label(self._current_frame, text="Help").pack(pady=10)
        text_widget = Text(self._current_frame, wrap="word", height=20)
        text_widget.insert("1.0", help_text)
        text_widget.config(state="disabled")
        text_widget.pack(fill="both", expand=True)
        back_button = ttk.Button(
            self._current_frame,
            text="Back",
            command=self._show_main_view,
            takefocus=True,
        )
        back_button.pack(pady=5)
        back_button.bind("<Return>", lambda e: self._show_main_view())
        back_button.focus_set()
