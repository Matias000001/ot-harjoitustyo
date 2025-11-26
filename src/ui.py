# src/ui.py
from tkinter import ttk, filedialog, messagebox, Text
import io
import os
import contextlib

from encryption.key_manager import get_key_from_password
from encryption.encryptor import Encryptor
from encryption.decryptor import Decryptor
from introduction import print_help

# Parts of this code were inspired by AI

class UI:
    def __init__(self, root):
        self.root = root
        self.encryptor = None
        self.decryptor = None
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
        ttk.Button(
            self._current_frame,
            text="Continue",
            command=self._handle_password_ok,
        ).grid(row=3, column=0, columnspan=2, pady=10)

    def _handle_password_ok(self):
        pw1 = self._pw1_var.get()
        pw2 = self._pw2_var.get()
        if not pw1:
            messagebox.showerror("Error", "Password cannot be empty.")
            return
        if pw1 != pw2:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        key = get_key_from_password(pw1)
        self.encryptor = Encryptor(key)
        self.decryptor = Decryptor(key)
        self._show_main_view()

    def _show_main_view(self):
        self._clear_frame()
        ttk.Label(self._current_frame, text="CipherVault").pack(pady=10)
        ttk.Button(
            self._current_frame,
            text="Encrypt file",
            command=self.encrypt_file,
        ).pack(pady=5)
        ttk.Button(
            self._current_frame,
            text="Decrypt file",
            command=self.decrypt_file,
        ).pack(pady=5)
        ttk.Button(
            self._current_frame,
            text="Help",
            command=self.show_help,
        ).pack(pady=5)
        ttk.Button(
            self._current_frame,
            text="Quit",
            command=self.root.quit,
        ).pack(pady=5)

    def encrypt_file(self):
        inp = filedialog.askopenfilename(title="Select file to encrypt")
        if not inp:
            return
        out = filedialog.asksaveasfilename(title="Enter output file")
        if not out:
            return
        ok = self.encryptor.encrypt_file(inp, out)
        if ok:
            try:
                os.remove(inp)
                messagebox.showinfo(
                    "Result",
                    "File encrypted.\nOriginal (unencrypted) file deleted."
                )
            except OSError:
                messagebox.showwarning(
                    "Result",
                    "File encrypted.\nWarning: failed to delete original file."
                )
        else:
            messagebox.showerror("Error", "Encryption failed.")

    def decrypt_file(self):
        inp = filedialog.askopenfilename(title="Select file to decrypt")
        if not inp:
            return
        out = filedialog.asksaveasfilename(title="Enter output file")
        if not out:
            return
        ok = self.decryptor.decrypt_file(inp, out)
        if ok:
            try:
                os.remove(inp)
                messagebox.showinfo(
                    "Result",
                    "File decrypted.\nEncrypted file deleted."
                )
            except OSError:
                messagebox.showwarning(
                    "Result",
                    "File decrypted.\nWarning: failed to delete encrypted file."
                )
        else:
            messagebox.showerror("Error", "Decryption failed.")
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
        ttk.Button(
            self._current_frame,
            text="Back",
            command=self._show_main_view,
        ).pack(pady=5)
