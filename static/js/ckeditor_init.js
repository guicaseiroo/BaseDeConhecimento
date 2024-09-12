import {
    ClassicEditor,
    Essentials,
    Paragraph,
    Bold,
    Italic,
    Font,
    Underline,
    Strikethrough,
    BlockQuote,
    Heading,
    Link,
    List,
    Image,
    ImageToolbar,
    ImageCaption,
    ImageStyle,
    ImageResize,
    Table,
    TableToolbar,
    MediaEmbed,
    Code,
    CodeBlock,
    Highlight,
    SimpleUploadAdapter
} from 'ckeditor5';

function initializeCkEditor(selector) {
    ClassicEditor
        .create(document.querySelector(selector), {
            plugins: [
                Essentials, Paragraph, Bold, Italic, Font, Underline, Strikethrough,
                BlockQuote, Heading, Link, List, Image, ImageToolbar, ImageCaption,
                ImageStyle, ImageResize, Table, TableToolbar, MediaEmbed, Code,
                CodeBlock, Highlight, SimpleUploadAdapter
            ],
            toolbar: [
                'undo', 'redo', '|', 'heading', '|', 'bold', 'italic', 'underline', 'strikethrough', '|',
                'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', '|',
                'link', 'blockquote', '|', 'bulletedList', 'numberedList', '|',
                'insertTable', '|', 'imageUpload', 'mediaEmbed', '|', 'code', 'codeBlock', 'highlight'
            ],
            image: {
                toolbar: ['imageTextAlternative', 'imageStyle:full', 'imageStyle:side', 'imageResize'],
                upload: {
                    types: ['png', 'jpeg', 'jpg', 'gif']
                }
            },
            table: {
                contentToolbar: ['tableColumn', 'tableRow', 'mergeTableCells']
            },
            simpleUpload: {
                uploadUrl: '/upload',  // Endpoint de upload para imagens
                headers: {
                    'X-CSRF-TOKEN': document.querySelector('[name=csrfmiddlewaretoken]').value,  // Token CSRF
                    Authorization: 'Bearer <token>'  // Ajuste se necessário
                }
            }
        })
        .then(editor => {
            window.editor = editor;
        })
        .catch(error => {
            console.error(error);
        });

    // Sincroniza o conteúdo do CKEditor com o textarea antes da submissão do formulário
    document.querySelector('form').addEventListener('submit', function(event) {
        if (window.editor) {
            window.editor.updateSourceElement();  // Atualiza o textarea original com o conteúdo do CKEditor
        }
    });
}

export { initializeCkEditor };
